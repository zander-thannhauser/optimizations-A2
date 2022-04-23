.data
    .string .str_const_1, "nope\\n"
    .string .Lglobal_x, "hello\\n"
.text
.frame main, 0 
    loadI .str_const_1 => %vr5
    i2i %vr5 => %vr6
    loadI .Lglobal_x => %vr7
    swrite %vr7
    swrite %vr6
    ret
