################################################################################
# Automatically-generated file. Do not edit!
################################################################################

-include ../makefile.init

RM := rm -rf

# All of the sources participating in the build are defined here
-include sources.mk
-include Startup/subdir.mk
-include Src/subdir.mk
-include subdir.mk
-include objects.mk

ifneq ($(MAKECMDGOALS),clean)
ifneq ($(strip $(C_DEPS)),)
-include $(C_DEPS)
endif
endif

-include ../makefile.defs

# Add inputs and outputs from these tool invocations to the build variables 
EXECUTABLES += \
Boot_Flash.elf \

SIZE_OUTPUT += \
default.size.stdout \

OBJDUMP_LIST += \
Boot_Flash.list \

OBJCOPY_BIN += \
Boot_Flash.bin \


# All Target
all: Boot_Flash.elf secondary-outputs

# Tool invocations
Boot_Flash.elf: $(OBJS) $(USER_OBJS) D:\Teaching_Documents\Bootloader\Flash\Boot_Flash\STM32F401RETX_FLASH.ld
	arm-none-eabi-gcc -o "Boot_Flash.elf" @"objects.list" $(USER_OBJS) $(LIBS) -mcpu=cortex-m4 -T"D:\Teaching_Documents\Bootloader\Flash\Boot_Flash\STM32F401RETX_FLASH.ld" --specs=nosys.specs -Wl,-Map="Boot_Flash.map" -Wl,--gc-sections -static -L"D:\IOT302_Funix\SDK_1.0.3_NUCLEO-F401RE\lib_stm" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -Wl,--start-group -lc -lm -Wl,--end-group
	@echo 'Finished building target: $@'
	@echo ' '

default.size.stdout: $(EXECUTABLES)
	arm-none-eabi-size  $(EXECUTABLES)
	@echo 'Finished building: $@'
	@echo ' '

Boot_Flash.list: $(EXECUTABLES)
	arm-none-eabi-objdump -h -S $(EXECUTABLES) > "Boot_Flash.list"
	@echo 'Finished building: $@'
	@echo ' '

Boot_Flash.bin: $(EXECUTABLES)
	arm-none-eabi-objcopy  -O binary $(EXECUTABLES) "Boot_Flash.bin"
	@echo 'Finished building: $@'
	@echo ' '

# Other Targets
clean:
	-$(RM) *
	-@echo ' '

secondary-outputs: $(SIZE_OUTPUT) $(OBJDUMP_LIST) $(OBJCOPY_BIN)

.PHONY: all clean dependents
.SECONDARY:

-include ../makefile.targets
