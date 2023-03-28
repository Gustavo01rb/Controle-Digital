clear ;
clc ;
d =[1];
t = -1:.01:1;
h =0;
clf ();
figure (0);
a= gca ();
a.x_location="origin";

for i=1:length(t)
    if t(i)<0
      h =0;
    else
    h=d;
    plot2d3 (i-101 ,h)
    plot (i-101 ,h, '.r' )
    xtitle ( 'Resposta ao impulso de um acumulador' , 't', 'Y' );
    a.children.children.thickness =1;
    a.children.children.foreground =2;
    end
end
disp (h, 'The impul s e r e s p o n s e o f Accumulator i s =' )
