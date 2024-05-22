%% AMPLITUDE OFF-AXIS FOURIER HOLOGRAM SYNTHESIS for Holo_memory
% 
% 
% 
clc
clear
close all

%% Input prior parameters

title0   = 'Input prior parameters';
prompt0  = {...
        'Hologram height (pixels):',...
        'Hologram width (pixels):', ... %'Number of objects',...
        'Add phase mask (0 - no, no 1 - yes):',... %'Bit size (px):'
        };
    
lines0 = 1.2;
def0 = {'50','50','1','0','2'};
answer0 = inputdlg(prompt0,title0,lines0,def0);
Xrez = str2double(answer0{1});
Yrez = str2double(answer0{2});
N_obj = 1;
phasemask = str2double(answer0{3});

choice = questdlg('Choose dimensionality', ...
 'Lens dimension', ...
 '1D','2D','2D');

% file_type = questdlg('Sourse file type', ...
%  'Lens dimension', ...
%  'mat','bmp','bmp');

file_type = 'bmp';

%% Load objects (pic)

pic = cell(1,N_obj);

switch file_type
    case 'bmp'

for n = 1:N_obj
    newpath = '/Users/john/SCIENCE/MSTU/HOLO_Memory/objects/*.bmp'; % <----- my macBook dir
%     newpath = '*.bmp';
    [newpicfile,newpath] = uigetfile(newpath,'Open Object File');
    picfile = [newpath,newpicfile];
    if newpath == 0
        break;
    end;
    pic1 = double(imread(picfile));
    pic{n} = pic1(:,:,1);
end

    case 'mat'
        
for n = 1:N_obj
    newpath = '*.mat'; % <----- my macBook dir
    [newpicfile,newpath] = uigetfile(newpath,'Open Object File');
    picfile=[newpath,newpicfile];
    if newpath == 0
        break;
    end;
    fpic = load(picfile);
    pic{n} = double(fpic.a);
end
end

rez = size(pic{1}); % <------- object sizes
figure;
imshow(mat2gray(pic{1}));

%% ADD PHASE MASK TO pic

%         ampMask = int8(rand(rez(1), rez(2)));
%         ampMask(ampMask==0) = -1;        
%         obj = pic{1};
%         obj(rez(1)+1,rez(2)+1)=0;
%         
%         for h = 1:rez(1)
%             for w = 1:rez(2)
%                 if obj(h, w) > 50
%                     if obj(h, w+1) > 50
%                        ampMask(h, w+1) = ampMask(h, w);
%                     end
%                     if obj(h+1, w+1) > 50
%                         ampMask(h+1, w+1) = ampMask(h, w);
%                     end
%                     if obj(h+1, w) > 50
%                         ampMask(h+1, w) = ampMask(h, w);
%                     end
%                     if (w > 1) && (obj(h+1, w-1) > 50)
%                         ampMask(h+1, w-1) = ampMask(h, w);
%                     end
%                 else
%                     ampMask(h, w) = 0;
%                 end
%             end
%         end
%         pic{n} = pic{n}.*double(ampMask);
%         figure(227);
%         imagesc(ampMask);
%         colormap(jet);
%         colorbar;
%         title('AMP MASK');

switch phasemask 
    case(1)
 
        
% % “”“ ¬Õ»Ã¿“≈À‹ÕŒ!
% mask = uint8(rand(rez(1), rez(2)));
% %         
% %        save('Masktrue.mat','mask','-mat');
% 
%         obj = pic{1};
%         obj(rez(1)+1,rez(2)+1)=0;
%         
%         for h = 1:rez(1)
%             for w = 1:rez(2)
%                 if (obj(h, w) > 0) || (obj(h, w) < 0)
%                     if obj(h, w+1) == obj(h, w)
%                        mask(h, w+1) = mask(h, w);
%                     end
%                     if obj(h+1, w+1) == obj(h, w)
%                         mask(h+1, w+1) = mask(h, w);
%                     end
%                     if obj(h+1, w) == obj(h, w)
%                         mask(h+1, w) = mask(h, w);
%                     end
%                     if (w > 1) && (obj(h+1, w-1) == obj(h, w))
%                         mask(h+1, w-1) = mask(h, w);
%                     end
%                 else
%                     mask(h, w) = 0;
%                 end
%             end
%         end
%         
%         pic{n} = pic{n}.*exp(1i*pi.*double(mask));
%         figure(2);
%         imagesc(mask);
%         colormap(jet);
%         colorbar;
%         title('PHASE MASK');

mask = zeros(rez(1), rez(2));
mask1 = round(rand(rez(1),rez(2)));
mask2 = round(-1*rand(rez(1),rez(2)));

[A,B] = size(mask);
mask = mask1+mask2;
mask(mask<-0.1) = -1;
mask(mask>0.1) = 1;
fi = pi*mask;

figure;
imshow(fi);

        pic{1}=pic{1}.*exp(1i*fi);

        figure(2);
        imagesc(mask);
        colormap(jet);
        colorbar;
        title('PHASE MASK');
    case(0)
                
end




%% TRANSFORM pic TO REFERENCE IMAGE p0 [Xrez, Yrez]

shift = 0;

p0 = zeros(Xrez,Yrez);

if N_obj == 2
    p0(Xrez*3/4 - rez(1)/2:Xrez*3/4 + rez(1)/2-1, Yrez/4-(rez(2)/2):Yrez/4+rez(2)/2-1) = pic{1};
    p0(Xrez/4 - rez(1)/2:Xrez/4 + rez(1)/2-1, Yrez/4-(rez(2)/2):Yrez/4+rez(2)/2-1) = pic{2};
%     p0(Xrez/4 - rez(1)/2:Xrez/4 + rez(1)/2-1, Yrez/2-(rez(2)/2):Yrez/2+rez(2)/2-1) = pic{3};

else
    p0(round(Xrez/2) -round(rez(1)/2):round(Xrez/2) - 2 + round(rez(1)/2), ...
        round(Yrez/4) - round(rez(2)/2) + 1 + shift:round(Yrez/4) + round(rez(2)/2) - 1 + shift) = pic{1};
%   p0(Xrez/2-rez(1)/2-150:Xrez/2-1+rez(1)/2-150, Yrez/4-(rez(2)/2):Yrez/4+rez(2)/2-1) = pic{1};
    
end
% 
% % p0(Xrez/2-rez(1)/2-150:Xrez/2-1+rez(1)/2-150, Yrez/4-round(rez(2)/2)-50:Yrez/4+round(rez(2)/2)-2-50) = pic;
% % p0(Xrez/2-rez(1)/2+150:Xrez/2-1+rez(1)/2+150, Yrez/4-round(rez(2)/2)-50:Yrez/4+round(rez(2)/2)-2-50) = pic;
% % p0(Xrez/4-round(rez(1)/2):Xrez/4+round(rez(1)/2)-1, Yrez/2-rez(2)/2:Yrez/2-1+rez(2)/2) = pic;
%  
% % p=p0.*exp(i.*f0);

% p0=pic{1};
pa=abs(p0);
mpa=max(max(pa));
pf=angle(p0);

figure;
imshow(mat2gray(angle(p0)));

%% REFERENCE IMAGE FOURIER TRANSFORM fp

cgh = double(zeros(Xrez, Yrez));
switch choice
    case '1D'
        for h=1:Xrez
            p = ifftshift(p0(h, :));
            fp=fftshift(fft(p, [], 2));
            cgh(h, :) = real(fp);
            mincgh=min(min(cgh(h, :)));
            cgh(h, :)=cgh(h, :)-mincgh;
            mcgh=max(max(cgh(h, :)));
            cgh(h, :)=cgh(h, :)./mcgh;
        end
        
    case '2D'
        p = ifftshift(p0);
        fp = fft2(p);
        fp = fftshift(fp);
        cgh = real(fp);
        mincgh=min(min(cgh));
        cgh=cgh-mincgh;
        mcgh=max(max(cgh));
        cgh=cgh./mcgh;
end

% 


fpa=abs(fp);
mfpa=max(max(fpa));
fpf=angle(fp);

%% HOLOGRAM SYNTHESIS cgh = C + 2Re [H exp (-j2*piDx )] real

% cgh = 255*cgh;

pr = graythresh(cgh); % ŒÔÚËÏ‡Î¸Ì˚È ÔÓÓ„ ÔÓ ÏÂÚÓ‰Û ŒˆÛ
cgh_BW = im2bw (cgh,pr);

imshow(mat2gray(cgh_BW));
imwrite(uint8(cgh_BW), 'cgh_BW.bmp', 'BMP');




figure(6);
imagesc(cgh);
colormap(gray);
caxis([0 255]);
axis image;
title('SYNTHESIZED HOLOGRAM');



% cgh=exp(1i.*2.*pi.*cgh);     %<- convert to phase hologram

%% HOLOGRAM RECONSTRUCTION

intCGH = uint8(cgh/16)*16;

ph=ifftshift(intCGH);
% ph=ifft(ph, [], 2);

switch choice
    case '1D'
        ph = ifft(ph, [], 2);
    case '2D'
        ph = ifft2(ph);
end

ph=fftshift(ph);

pha = abs(ph);
phf=angle(ph);

% % remove zero order
% 
% zerorder=pha(Xrez./2+1,Yrez./2+1);
% pha(Xrez./2+1,Yrez./2+1) = 0;
% pha(pha>10) = 10;
% mpha=max(max(pha));

figure(8);
imagesc(pha);
colormap(gray);
% caxis([0 mpha]);
axis image;
title('RECONSTRUCTED AMPLITUDE');

% imwrite(uint8(pha), 'pha.bmp', 'BMP');



%% RECOVERED OBJECT

pich=ph(Xrez/2-rez(1)/2:Xrez/2-1+rez(1)/2, Yrez/4-round(rez(2)/2):Yrez/4+round(rez(2)/2)-2);
picha = abs(pich);
pichf=angle(pich);
mpicha=max(max(picha));

%% DIFRACTION EFFICIENCY

zeroRegWidth = 8;

pich=pha(Xrez/2-rez(1)/2:Xrez/2-1+rez(1)/2, Yrez/4-round(rez(2)/2):Yrez/4+round(rez(2)/2)-2);

DE = sum(sum(pich))/sum(sum(pha));

% imageReg = zeros(size(pich)/2 + zeroRegWidth);

imageReg = pha(Xrez/2-rez(1)/2 - zeroRegWidth:Xrez/2-1, Yrez/4 - zeroRegWidth-round(rez(2)/2):Yrez/4 -2);
imageReg = uint8(imageReg*255/max(max(imageReg)));

figure(14);
imagesc(pich);
colormap(gray);
% caxis([0 mpicha]);
axis image;
title(['OBJECT AMPLITUDE, DE = ', num2str(DE)]);
% 
figure
imagesc(log(abs(cgh)+1).^2), colormap gray;
% imwrite(mat2gray(log(abs(cgh)+1).^2), '2pxHoloLog.png', 'png');



