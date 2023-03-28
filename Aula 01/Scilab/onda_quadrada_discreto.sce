clc ;
clear ;
clf ();
a= gca ();
figure (0);
a.x_location ="origin";

x =[0:1:80];

y1=sin(x *.05* %pi);

y2=sin(x*.15*%pi);
y3=sin(x*.25*%pi);
y4=y1+y2/3+ y3/5;
plot2d3(x,y4 ,2)
plot (x,y4 , 'r.' )
xtitle ( 'Aproximação de uma onda quadrada' , 'x' , 'y4' );
a.children.children.thickness =3;
