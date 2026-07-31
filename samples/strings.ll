; String heavy program - many string constants
define void @print_messages() {
entry:
  %msg1 = alloca [13 x i8]
  %msg2 = alloca [11 x i8]
  %msg3 = alloca [15 x i8]
  %msg4 = alloca [10 x i8]
  %key1 = alloca [8 x i8]
  %key2 = alloca [16 x i8]
  %pass = alloca [12 x i8]
  ret void
}

define i32 @validate() {
entry:
  %token = alloca [20 x i8]
  %secret = alloca [14 x i8]
  %result = alloca i32
  store i32 1, i32* %result
  %val = load i32, i32* %result
  ret i32 %val
}

define i32 @main() {
entry:
  %status = alloca i32
  store i32 0, i32* %status
  %s = load i32, i32* %status
  ret i32 %s
}