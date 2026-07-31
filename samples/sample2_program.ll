; ModuleID = 'samples\sample2_program.c'
source_filename = "samples\\sample2_program.c"
target datalayout = "e-m:w-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-windows-msvc19.29.30159"

%struct.TIME = type { i32, i32, i32 }

$sprintf = comdat any

$vsprintf = comdat any

$_snprintf = comdat any

$_vsnprintf = comdat any

$printf = comdat any

$scanf = comdat any

$_vsprintf_l = comdat any

$_vsnprintf_l = comdat any

$__local_stdio_printf_options = comdat any

$_vfprintf_l = comdat any

$_vfscanf_l = comdat any

$__local_stdio_scanf_options = comdat any

$"??_C@_0BI@ELBKBBME@Enter?5the?5start?5time?4?5?6?$AA@" = comdat any

$"??_C@_0CD@NNDODBOJ@Enter?5hours?0?5minutes?5and?5seconds@" = comdat any

$"??_C@_08OOHKHLPO@?$CFd?5?$CFd?5?$CFd?$AA@" = comdat any

$"??_C@_0BH@NCEJLGIB@Enter?5the?5stop?5time?4?5?6?$AA@" = comdat any

$"??_C@_0BO@PPOGNALI@?6Time?5Difference?3?5?$CFd?3?$CFd?3?$CFd?5?9?5?$AA@" = comdat any

$"??_C@_09IEECDAC@?$CFd?3?$CFd?3?$CFd?5?$AA@" = comdat any

$"??_C@_0M@PDGKPJAO@?$DN?5?$CFd?3?$CFd?3?$CFd?6?$AA@" = comdat any

@"??_C@_0BI@ELBKBBME@Enter?5the?5start?5time?4?5?6?$AA@" = linkonce_odr dso_local unnamed_addr constant [24 x i8] c"Enter the start time. \0A\00", comdat, align 1
@"??_C@_0CD@NNDODBOJ@Enter?5hours?0?5minutes?5and?5seconds@" = linkonce_odr dso_local unnamed_addr constant [35 x i8] c"Enter hours, minutes and seconds: \00", comdat, align 1
@"??_C@_08OOHKHLPO@?$CFd?5?$CFd?5?$CFd?$AA@" = linkonce_odr dso_local unnamed_addr constant [9 x i8] c"%d %d %d\00", comdat, align 1
@"??_C@_0BH@NCEJLGIB@Enter?5the?5stop?5time?4?5?6?$AA@" = linkonce_odr dso_local unnamed_addr constant [23 x i8] c"Enter the stop time. \0A\00", comdat, align 1
@"??_C@_0BO@PPOGNALI@?6Time?5Difference?3?5?$CFd?3?$CFd?3?$CFd?5?9?5?$AA@" = linkonce_odr dso_local unnamed_addr constant [30 x i8] c"\0ATime Difference: %d:%d:%d - \00", comdat, align 1
@"??_C@_09IEECDAC@?$CFd?3?$CFd?3?$CFd?5?$AA@" = linkonce_odr dso_local unnamed_addr constant [10 x i8] c"%d:%d:%d \00", comdat, align 1
@"??_C@_0M@PDGKPJAO@?$DN?5?$CFd?3?$CFd?3?$CFd?6?$AA@" = linkonce_odr dso_local unnamed_addr constant [12 x i8] c"= %d:%d:%d\0A\00", comdat, align 1
@__local_stdio_printf_options._OptionsStorage = internal global i64 0, align 8
@__local_stdio_scanf_options._OptionsStorage = internal global i64 0, align 8

; Function Attrs: noinline nounwind optnone uwtable
define linkonce_odr dso_local i32 @sprintf(ptr noundef %0, ptr noundef %1, ...) #0 comdat {
  %3 = alloca ptr, align 8
  %4 = alloca ptr, align 8
  %5 = alloca i32, align 4
  %6 = alloca ptr, align 8
  store ptr %1, ptr %3, align 8
  store ptr %0, ptr %4, align 8
  call void @llvm.va_start.p0(ptr %6)
  %7 = load ptr, ptr %6, align 8
  %8 = load ptr, ptr %3, align 8
  %9 = load ptr, ptr %4, align 8
  %10 = call i32 @_vsprintf_l(ptr noundef %9, ptr noundef %8, ptr noundef null, ptr noundef %7)
  store i32 %10, ptr %5, align 4
  call void @llvm.va_end.p0(ptr %6)
  %11 = load i32, ptr %5, align 4
  ret i32 %11
}

; Function Attrs: noinline nounwind optnone uwtable
define linkonce_odr dso_local i32 @vsprintf(ptr noundef %0, ptr noundef %1, ptr noundef %2) #0 comdat {
  %4 = alloca ptr, align 8
  %5 = alloca ptr, align 8
  %6 = alloca ptr, align 8
  store ptr %2, ptr %4, align 8
  store ptr %1, ptr %5, align 8
  store ptr %0, ptr %6, align 8
  %7 = load ptr, ptr %4, align 8
  %8 = load ptr, ptr %5, align 8
  %9 = load ptr, ptr %6, align 8
  %10 = call i32 @_vsnprintf_l(ptr noundef %9, i64 noundef -1, ptr noundef %8, ptr noundef null, ptr noundef %7)
  ret i32 %10
}

; Function Attrs: noinline nounwind optnone uwtable
define linkonce_odr dso_local i32 @_snprintf(ptr noundef %0, i64 noundef %1, ptr noundef %2, ...) #0 comdat {
  %4 = alloca ptr, align 8
  %5 = alloca i64, align 8
  %6 = alloca ptr, align 8
  %7 = alloca i32, align 4
  %8 = alloca ptr, align 8
  store ptr %2, ptr %4, align 8
  store i64 %1, ptr %5, align 8
  store ptr %0, ptr %6, align 8
  call void @llvm.va_start.p0(ptr %8)
  %9 = load ptr, ptr %8, align 8
  %10 = load ptr, ptr %4, align 8
  %11 = load i64, ptr %5, align 8
  %12 = load ptr, ptr %6, align 8
  %13 = call i32 @_vsnprintf(ptr noundef %12, i64 noundef %11, ptr noundef %10, ptr noundef %9)
  store i32 %13, ptr %7, align 4
  call void @llvm.va_end.p0(ptr %8)
  %14 = load i32, ptr %7, align 4
  ret i32 %14
}

; Function Attrs: noinline nounwind optnone uwtable
define linkonce_odr dso_local i32 @_vsnprintf(ptr noundef %0, i64 noundef %1, ptr noundef %2, ptr noundef %3) #0 comdat {
  %5 = alloca ptr, align 8
  %6 = alloca ptr, align 8
  %7 = alloca i64, align 8
  %8 = alloca ptr, align 8
  store ptr %3, ptr %5, align 8
  store ptr %2, ptr %6, align 8
  store i64 %1, ptr %7, align 8
  store ptr %0, ptr %8, align 8
  %9 = load ptr, ptr %5, align 8
  %10 = load ptr, ptr %6, align 8
  %11 = load i64, ptr %7, align 8
  %12 = load ptr, ptr %8, align 8
  %13 = call i32 @_vsnprintf_l(ptr noundef %12, i64 noundef %11, ptr noundef %10, ptr noundef null, ptr noundef %9)
  ret i32 %13
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca %struct.TIME, align 4
  %3 = alloca %struct.TIME, align 4
  %4 = alloca %struct.TIME, align 4
  %5 = alloca %struct.TIME, align 4
  %6 = alloca %struct.TIME, align 4
  store i32 0, ptr %1, align 4
  %7 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0BI@ELBKBBME@Enter?5the?5start?5time?4?5?6?$AA@")
  %8 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0CD@NNDODBOJ@Enter?5hours?0?5minutes?5and?5seconds@")
  %9 = getelementptr inbounds nuw %struct.TIME, ptr %2, i32 0, i32 0
  %10 = getelementptr inbounds nuw %struct.TIME, ptr %2, i32 0, i32 1
  %11 = getelementptr inbounds nuw %struct.TIME, ptr %2, i32 0, i32 2
  %12 = call i32 (ptr, ...) @scanf(ptr noundef @"??_C@_08OOHKHLPO@?$CFd?5?$CFd?5?$CFd?$AA@", ptr noundef %11, ptr noundef %10, ptr noundef %9)
  %13 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0BH@NCEJLGIB@Enter?5the?5stop?5time?4?5?6?$AA@")
  %14 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0CD@NNDODBOJ@Enter?5hours?0?5minutes?5and?5seconds@")
  %15 = getelementptr inbounds nuw %struct.TIME, ptr %3, i32 0, i32 0
  %16 = getelementptr inbounds nuw %struct.TIME, ptr %3, i32 0, i32 1
  %17 = getelementptr inbounds nuw %struct.TIME, ptr %3, i32 0, i32 2
  %18 = call i32 (ptr, ...) @scanf(ptr noundef @"??_C@_08OOHKHLPO@?$CFd?5?$CFd?5?$CFd?$AA@", ptr noundef %17, ptr noundef %16, ptr noundef %15)
  call void @llvm.memcpy.p0.p0.i64(ptr align 4 %5, ptr align 4 %2, i64 12, i1 false)
  call void @llvm.memcpy.p0.p0.i64(ptr align 4 %6, ptr align 4 %3, i64 12, i1 false)
  call void @differenceBetweenTimePeriod(ptr dead_on_return noundef %5, ptr dead_on_return noundef %6, ptr noundef %4)
  %19 = getelementptr inbounds nuw %struct.TIME, ptr %2, i32 0, i32 0
  %20 = load i32, ptr %19, align 4
  %21 = getelementptr inbounds nuw %struct.TIME, ptr %2, i32 0, i32 1
  %22 = load i32, ptr %21, align 4
  %23 = getelementptr inbounds nuw %struct.TIME, ptr %2, i32 0, i32 2
  %24 = load i32, ptr %23, align 4
  %25 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0BO@PPOGNALI@?6Time?5Difference?3?5?$CFd?3?$CFd?3?$CFd?5?9?5?$AA@", i32 noundef %24, i32 noundef %22, i32 noundef %20)
  %26 = getelementptr inbounds nuw %struct.TIME, ptr %3, i32 0, i32 0
  %27 = load i32, ptr %26, align 4
  %28 = getelementptr inbounds nuw %struct.TIME, ptr %3, i32 0, i32 1
  %29 = load i32, ptr %28, align 4
  %30 = getelementptr inbounds nuw %struct.TIME, ptr %3, i32 0, i32 2
  %31 = load i32, ptr %30, align 4
  %32 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_09IEECDAC@?$CFd?3?$CFd?3?$CFd?5?$AA@", i32 noundef %31, i32 noundef %29, i32 noundef %27)
  %33 = getelementptr inbounds nuw %struct.TIME, ptr %4, i32 0, i32 0
  %34 = load i32, ptr %33, align 4
  %35 = getelementptr inbounds nuw %struct.TIME, ptr %4, i32 0, i32 1
  %36 = load i32, ptr %35, align 4
  %37 = getelementptr inbounds nuw %struct.TIME, ptr %4, i32 0, i32 2
  %38 = load i32, ptr %37, align 4
  %39 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0M@PDGKPJAO@?$DN?5?$CFd?3?$CFd?3?$CFd?6?$AA@", i32 noundef %38, i32 noundef %36, i32 noundef %34)
  ret i32 0
}

; Function Attrs: noinline nounwind optnone uwtable
define linkonce_odr dso_local i32 @printf(ptr noundef %0, ...) #0 comdat {
  %2 = alloca ptr, align 8
  %3 = alloca i32, align 4
  %4 = alloca ptr, align 8
  store ptr %0, ptr %2, align 8
  call void @llvm.va_start.p0(ptr %4)
  %5 = load ptr, ptr %4, align 8
  %6 = load ptr, ptr %2, align 8
  %7 = call ptr @__acrt_iob_func(i32 noundef 1)
  %8 = call i32 @_vfprintf_l(ptr noundef %7, ptr noundef %6, ptr noundef null, ptr noundef %5)
  store i32 %8, ptr %3, align 4
  call void @llvm.va_end.p0(ptr %4)
  %9 = load i32, ptr %3, align 4
  ret i32 %9
}

; Function Attrs: noinline nounwind optnone uwtable
define linkonce_odr dso_local i32 @scanf(ptr noundef %0, ...) #0 comdat {
  %2 = alloca ptr, align 8
  %3 = alloca i32, align 4
  %4 = alloca ptr, align 8
  store ptr %0, ptr %2, align 8
  call void @llvm.va_start.p0(ptr %4)
  %5 = load ptr, ptr %4, align 8
  %6 = load ptr, ptr %2, align 8
  %7 = call ptr @__acrt_iob_func(i32 noundef 0)
  %8 = call i32 @_vfscanf_l(ptr noundef %7, ptr noundef %6, ptr noundef null, ptr noundef %5)
  store i32 %8, ptr %3, align 4
  call void @llvm.va_end.p0(ptr %4)
  %9 = load i32, ptr %3, align 4
  ret i32 %9
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local void @differenceBetweenTimePeriod(ptr dead_on_return noundef %0, ptr dead_on_return noundef %1, ptr noundef %2) #0 {
  %4 = alloca ptr, align 8
  %5 = alloca ptr, align 8
  %6 = alloca ptr, align 8
  store ptr %2, ptr %4, align 8
  store ptr %1, ptr %5, align 8
  store ptr %0, ptr %6, align 8
  br label %7

7:                                                ; preds = %13, %3
  %8 = getelementptr inbounds nuw %struct.TIME, ptr %0, i32 0, i32 0
  %9 = load i32, ptr %8, align 4
  %10 = getelementptr inbounds nuw %struct.TIME, ptr %1, i32 0, i32 0
  %11 = load i32, ptr %10, align 4
  %12 = icmp sgt i32 %9, %11
  br i1 %12, label %13, label %20

13:                                               ; preds = %7
  %14 = getelementptr inbounds nuw %struct.TIME, ptr %1, i32 0, i32 1
  %15 = load i32, ptr %14, align 4
  %16 = add nsw i32 %15, -1
  store i32 %16, ptr %14, align 4
  %17 = getelementptr inbounds nuw %struct.TIME, ptr %1, i32 0, i32 0
  %18 = load i32, ptr %17, align 4
  %19 = add nsw i32 %18, 60
  store i32 %19, ptr %17, align 4
  br label %7, !llvm.loop !8

20:                                               ; preds = %7
  %21 = getelementptr inbounds nuw %struct.TIME, ptr %1, i32 0, i32 0
  %22 = load i32, ptr %21, align 4
  %23 = getelementptr inbounds nuw %struct.TIME, ptr %0, i32 0, i32 0
  %24 = load i32, ptr %23, align 4
  %25 = sub nsw i32 %22, %24
  %26 = load ptr, ptr %4, align 8
  %27 = getelementptr inbounds nuw %struct.TIME, ptr %26, i32 0, i32 0
  store i32 %25, ptr %27, align 4
  br label %28

28:                                               ; preds = %34, %20
  %29 = getelementptr inbounds nuw %struct.TIME, ptr %0, i32 0, i32 1
  %30 = load i32, ptr %29, align 4
  %31 = getelementptr inbounds nuw %struct.TIME, ptr %1, i32 0, i32 1
  %32 = load i32, ptr %31, align 4
  %33 = icmp sgt i32 %30, %32
  br i1 %33, label %34, label %41

34:                                               ; preds = %28
  %35 = getelementptr inbounds nuw %struct.TIME, ptr %1, i32 0, i32 2
  %36 = load i32, ptr %35, align 4
  %37 = add nsw i32 %36, -1
  store i32 %37, ptr %35, align 4
  %38 = getelementptr inbounds nuw %struct.TIME, ptr %1, i32 0, i32 1
  %39 = load i32, ptr %38, align 4
  %40 = add nsw i32 %39, 60
  store i32 %40, ptr %38, align 4
  br label %28, !llvm.loop !10

41:                                               ; preds = %28
  %42 = getelementptr inbounds nuw %struct.TIME, ptr %1, i32 0, i32 1
  %43 = load i32, ptr %42, align 4
  %44 = getelementptr inbounds nuw %struct.TIME, ptr %0, i32 0, i32 1
  %45 = load i32, ptr %44, align 4
  %46 = sub nsw i32 %43, %45
  %47 = load ptr, ptr %4, align 8
  %48 = getelementptr inbounds nuw %struct.TIME, ptr %47, i32 0, i32 1
  store i32 %46, ptr %48, align 4
  %49 = getelementptr inbounds nuw %struct.TIME, ptr %1, i32 0, i32 2
  %50 = load i32, ptr %49, align 4
  %51 = getelementptr inbounds nuw %struct.TIME, ptr %0, i32 0, i32 2
  %52 = load i32, ptr %51, align 4
  %53 = sub nsw i32 %50, %52
  %54 = load ptr, ptr %4, align 8
  %55 = getelementptr inbounds nuw %struct.TIME, ptr %54, i32 0, i32 2
  store i32 %53, ptr %55, align 4
  %56 = load ptr, ptr %4, align 8
  %57 = getelementptr inbounds nuw %struct.TIME, ptr %56, i32 0, i32 2
  %58 = load i32, ptr %57, align 4
  %59 = icmp slt i32 %58, 0
  br i1 %59, label %60, label %65

60:                                               ; preds = %41
  %61 = load ptr, ptr %4, align 8
  %62 = getelementptr inbounds nuw %struct.TIME, ptr %61, i32 0, i32 2
  %63 = load i32, ptr %62, align 4
  %64 = add nsw i32 %63, 24
  store i32 %64, ptr %62, align 4
  br label %65

65:                                               ; preds = %60, %41
  ret void
}

; Function Attrs: nocallback nofree nounwind willreturn memory(argmem: readwrite)
declare void @llvm.memcpy.p0.p0.i64(ptr noalias writeonly captures(none), ptr noalias readonly captures(none), i64, i1 immarg) #1

; Function Attrs: nocallback nofree nosync nounwind willreturn
declare void @llvm.va_start.p0(ptr) #2

; Function Attrs: noinline nounwind optnone uwtable
define linkonce_odr dso_local i32 @_vsprintf_l(ptr noundef %0, ptr noundef %1, ptr noundef %2, ptr noundef %3) #0 comdat {
  %5 = alloca ptr, align 8
  %6 = alloca ptr, align 8
  %7 = alloca ptr, align 8
  %8 = alloca ptr, align 8
  store ptr %3, ptr %5, align 8
  store ptr %2, ptr %6, align 8
  store ptr %1, ptr %7, align 8
  store ptr %0, ptr %8, align 8
  %9 = load ptr, ptr %5, align 8
  %10 = load ptr, ptr %6, align 8
  %11 = load ptr, ptr %7, align 8
  %12 = load ptr, ptr %8, align 8
  %13 = call i32 @_vsnprintf_l(ptr noundef %12, i64 noundef -1, ptr noundef %11, ptr noundef %10, ptr noundef %9)
  ret i32 %13
}

; Function Attrs: nocallback nofree nosync nounwind willreturn
declare void @llvm.va_end.p0(ptr) #2

; Function Attrs: noinline nounwind optnone uwtable
define linkonce_odr dso_local i32 @_vsnprintf_l(ptr noundef %0, i64 noundef %1, ptr noundef %2, ptr noundef %3, ptr noundef %4) #0 comdat {
  %6 = alloca ptr, align 8
  %7 = alloca ptr, align 8
  %8 = alloca ptr, align 8
  %9 = alloca i64, align 8
  %10 = alloca ptr, align 8
  %11 = alloca i32, align 4
  store ptr %4, ptr %6, align 8
  store ptr %3, ptr %7, align 8
  store ptr %2, ptr %8, align 8
  store i64 %1, ptr %9, align 8
  store ptr %0, ptr %10, align 8
  %12 = load ptr, ptr %6, align 8
  %13 = load ptr, ptr %7, align 8
  %14 = load ptr, ptr %8, align 8
  %15 = load i64, ptr %9, align 8
  %16 = load ptr, ptr %10, align 8
  %17 = call ptr @__local_stdio_printf_options()
  %18 = load i64, ptr %17, align 8
  %19 = or i64 %18, 1
  %20 = call i32 @__stdio_common_vsprintf(i64 noundef %19, ptr noundef %16, i64 noundef %15, ptr noundef %14, ptr noundef %13, ptr noundef %12)
  store i32 %20, ptr %11, align 4
  %21 = load i32, ptr %11, align 4
  %22 = icmp slt i32 %21, 0
  br i1 %22, label %23, label %24

23:                                               ; preds = %5
  br label %26

24:                                               ; preds = %5
  %25 = load i32, ptr %11, align 4
  br label %26

26:                                               ; preds = %24, %23
  %27 = phi i32 [ -1, %23 ], [ %25, %24 ]
  ret i32 %27
}

declare dso_local i32 @__stdio_common_vsprintf(i64 noundef, ptr noundef, i64 noundef, ptr noundef, ptr noundef, ptr noundef) #3

; Function Attrs: noinline nounwind optnone uwtable
define linkonce_odr dso_local ptr @__local_stdio_printf_options() #0 comdat {
  ret ptr @__local_stdio_printf_options._OptionsStorage
}

; Function Attrs: noinline nounwind optnone uwtable
define linkonce_odr dso_local i32 @_vfprintf_l(ptr noundef %0, ptr noundef %1, ptr noundef %2, ptr noundef %3) #0 comdat {
  %5 = alloca ptr, align 8
  %6 = alloca ptr, align 8
  %7 = alloca ptr, align 8
  %8 = alloca ptr, align 8
  store ptr %3, ptr %5, align 8
  store ptr %2, ptr %6, align 8
  store ptr %1, ptr %7, align 8
  store ptr %0, ptr %8, align 8
  %9 = load ptr, ptr %5, align 8
  %10 = load ptr, ptr %6, align 8
  %11 = load ptr, ptr %7, align 8
  %12 = load ptr, ptr %8, align 8
  %13 = call ptr @__local_stdio_printf_options()
  %14 = load i64, ptr %13, align 8
  %15 = call i32 @__stdio_common_vfprintf(i64 noundef %14, ptr noundef %12, ptr noundef %11, ptr noundef %10, ptr noundef %9)
  ret i32 %15
}

declare dso_local ptr @__acrt_iob_func(i32 noundef) #3

declare dso_local i32 @__stdio_common_vfprintf(i64 noundef, ptr noundef, ptr noundef, ptr noundef, ptr noundef) #3

; Function Attrs: noinline nounwind optnone uwtable
define linkonce_odr dso_local i32 @_vfscanf_l(ptr noundef %0, ptr noundef %1, ptr noundef %2, ptr noundef %3) #0 comdat {
  %5 = alloca ptr, align 8
  %6 = alloca ptr, align 8
  %7 = alloca ptr, align 8
  %8 = alloca ptr, align 8
  store ptr %3, ptr %5, align 8
  store ptr %2, ptr %6, align 8
  store ptr %1, ptr %7, align 8
  store ptr %0, ptr %8, align 8
  %9 = load ptr, ptr %5, align 8
  %10 = load ptr, ptr %6, align 8
  %11 = load ptr, ptr %7, align 8
  %12 = load ptr, ptr %8, align 8
  %13 = call ptr @__local_stdio_scanf_options()
  %14 = load i64, ptr %13, align 8
  %15 = call i32 @__stdio_common_vfscanf(i64 noundef %14, ptr noundef %12, ptr noundef %11, ptr noundef %10, ptr noundef %9)
  ret i32 %15
}

declare dso_local i32 @__stdio_common_vfscanf(i64 noundef, ptr noundef, ptr noundef, ptr noundef, ptr noundef) #3

; Function Attrs: noinline nounwind optnone uwtable
define linkonce_odr dso_local ptr @__local_stdio_scanf_options() #0 comdat {
  ret ptr @__local_stdio_scanf_options._OptionsStorage
}

attributes #0 = { noinline nounwind optnone uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { nocallback nofree nounwind willreturn memory(argmem: readwrite) }
attributes #2 = { nocallback nofree nosync nounwind willreturn }
attributes #3 = { "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }

!llvm.dbg.cu = !{!0}
!llvm.module.flags = !{!2, !3, !4, !5, !6}
!llvm.ident = !{!7}

!0 = distinct !DICompileUnit(language: DW_LANG_C11, file: !1, producer: "clang version 22.1.1 (https://github.com/llvm/llvm-project fef02d48c08db859ef83f84232ed78bd9d1c323a)", isOptimized: false, runtimeVersion: 0, emissionKind: NoDebug, splitDebugInlining: false, nameTableKind: None)
!1 = !DIFile(filename: "samples\\sample2_program.c", directory: "D:\\llvm_obfuscator")
!2 = !{i32 2, !"Debug Info Version", i32 3}
!3 = !{i32 1, !"wchar_size", i32 2}
!4 = !{i32 8, !"PIC Level", i32 2}
!5 = !{i32 7, !"uwtable", i32 2}
!6 = !{i32 1, !"MaxTLSAlign", i32 65536}
!7 = !{!"clang version 22.1.1 (https://github.com/llvm/llvm-project fef02d48c08db859ef83f84232ed78bd9d1c323a)"}
!8 = distinct !{!8, !9}
!9 = !{!"llvm.loop.mustprogress"}
!10 = distinct !{!10, !9}
