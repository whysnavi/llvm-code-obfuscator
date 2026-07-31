; Sample LLVM IR - arithmetic program
define i32 @add(i32 %a, i32 %b) {
entry:
  %result = add i32 %a, %b
  ret i32 %result
}

; Function with branches
define i32 @max(i32 %a, i32 %b) {
entry:
  %cmp = icmp sgt i32 %a, %b
  br i1 %cmp, label %true_branch, label %false_branch
true_branch:
  ret i32 %a
false_branch:
  ret i32 %b
}

; Function with strings
define i32 @main() {
entry:
  %x = alloca i32
  %y = alloca i32
  store i32 10, i32* %x
  store i32 20, i32* %y
  %a = load i32, i32* %x
  %b = load i32, i32* %y
  %sum = add i32 %a, %b
  %msg = alloca [13 x i8]
  %key = alloca [8 x i8]
  ret i32 %sum
}