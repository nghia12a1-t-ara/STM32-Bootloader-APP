################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Src/main.c \
../Src/syscalls.c \
../Src/sysmem.c 

OBJS += \
./Src/main.o \
./Src/syscalls.o \
./Src/sysmem.o 

C_DEPS += \
./Src/main.d \
./Src/syscalls.d \
./Src/sysmem.d 


# Each subdirectory must supply rules for building sources it contributes
Src/main.o: ../Src/main.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DSTM32 -DSTM32F401RETx -DSTM32F4 -DDEBUG -c -I../Inc -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Drivers/CMSIS/Include" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Drivers/STM32F401RE_StdPeriph_Driver/inc" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Middle/button" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Middle/buzzer" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Middle/led" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Middle/rtos" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Middle/sensor" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Middle/serial" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Middle/ucglib" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Utilities" -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Src/main.d" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"
Src/syscalls.o: ../Src/syscalls.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DSTM32 -DSTM32F401RETx -DSTM32F4 -DDEBUG -c -I../Inc -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Drivers/CMSIS/Include" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Drivers/STM32F401RE_StdPeriph_Driver/inc" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Middle/button" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Middle/buzzer" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Middle/led" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Middle/rtos" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Middle/sensor" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Middle/serial" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Middle/ucglib" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Utilities" -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Src/syscalls.d" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"
Src/sysmem.o: ../Src/sysmem.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DSTM32 -DSTM32F401RETx -DSTM32F4 -DDEBUG -c -I../Inc -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Drivers/CMSIS/Include" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Drivers/STM32F401RE_StdPeriph_Driver/inc" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Middle/button" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Middle/buzzer" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Middle/led" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Middle/rtos" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Middle/sensor" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Middle/serial" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Middle/ucglib" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Utilities" -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Src/sysmem.d" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

