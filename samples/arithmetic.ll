; Arithmetic heavy program - many add/mul operations
define i32 @multiply(i32 %a, i32 %b) {
entry:
  %result = mul i32 %a, %b
  ret i32 %result
}

define i32 @calculate(i32 %x, i32 %y, i32 %z) {
entry:
  %sum1 = add i32 %x, %y
  %sum2 = add i32 %sum1, %z
  %mul1 = mul i32 %sum1, %sum2
  %mul2 = mul i32 %mul1, %x
  %final = add i32 %mul2, %sum2
  ret i32 %final
}

define i32 @main() {
entry:
  %a = alloca i32
  %b = alloca i32
  %c = alloca i32
  store i32 5, i32* %a
  store i32 10, i32* %b
  store i32 15, i32* %c
  %x = load i32, i32* %a
  %y = load i32, i32* %b
  %z = load i32, i32* %c
  %r1 = add i32 %x, %y
  %r2 = add i32 %r1, %z
  %r3 = add i32 %r2, %x
  ret i32 %r3
}