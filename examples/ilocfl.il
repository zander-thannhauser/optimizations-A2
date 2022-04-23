.data
    .float .float_const_0, 1.00000000
    .float .float_const_1, 3.00000000
    .float .float_const_2, 1.10000000
.text
.frame main, 12 
    loadI .float_const_0 => %vr1
    fload %vr1 => %vr2
    f2f %vr2 => %vr3
    
    loadI .float_const_1 => %vr4
    fload %vr4 => %vr5
    fmult %vr5, %vr3 => %vr6
    f2f %vr6 => %vr7
    
    loadI .float_const_2 => %vr8
    fload %vr8 => %vr9
    fsub %vr7, %vr9 => %vr10
    f2f %vr10 => %vr11
    
    fwrite %vr11
    
    ret
