clear ;
clc ;
n = -5:5;
    for i =1:length(n)
        if(n(i) >=1)
          h(i)=1/n(i);
        else
         h(i)=0;
        end
    end

Sum =0;
N =1:10000;
    for i =1: length (N)
        h(i) =(1/ N(i))^2;
    end

Energy = sum(h);

    if ( Energy <%inf ) then
      disp ('Sinal de energia') ;
      disp (Energy,'Energia do sinal=');
    else
     if ( Energy/length(N)<%inf) then
        disp ( 'Sina de Potencia' ) ;
    
    else
     disp ( 'Não é sinal de energia ou potencia' ) ;
    end
end
