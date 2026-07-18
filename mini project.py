class SmartDevice:
    def __init__(self, device_id, name):
        if not device_id or str(device_id).strip() == "":
            raise ValueError("Device ID cannot be empty.")

        self.__device_id = device_id
        self.__power_status = "OFF"
        self.name = name

    @property
    def device_id(self):
        return self.__device_id

    @property
    def power_status(self):
        return self.__power_status

    @power_status.setter
    def power_status(self, status):
        if status in ["ON", "OFF"]:
            self.__power_status = status
        else:
            raise ValueError("Power status must be ON or OFF.")

    def turn_on(self):
        self.__power_status = "ON"
        print(f"[{self.name}] has been powered ON.")

    def turn_off(self):
        self.__power_status = "OFF"
        print(f"[{self.name}] has been powered OFF.")

    def display_info(self):
        print(f"Device Name: {self.name}")
        print(f"Device ID: {self.device_id}")
        print(f"Power Status: {self.power_status}")


class TemperatureSensor(SmartDevice):
    def __init__(self, device_id, name, initial_temp=22.5):
        super().__init__(device_id, name)
        self.temperature = initial_temp

    def read_temperature(self):
        print(f"[{self.name}] Current Temperature: {self.temperature}°C")
        return self.temperature

    def display_info(self):
        super().display_info()
        print(f"Temperature: {self.temperature}°C")


class SmartLight(SmartDevice):
    def __init__(self, device_id, name, brightness=50):
        super().__init__(device_id, name)
        self.brightness = brightness

    @property
    def brightness(self):
        return self.__brightness

    @brightness.setter
    def brightness(self, value):
        if 0 <= value <= 100:
            self.__brightness = value
        else:
            raise ValueError("Brightness must be between 0 and 100.")

    def increase_brightness(self, amount=10):
        if self.power_status == "OFF":
            print(f"Cannot adjust brightness. [{self.name}] is OFF.")
            return

        self.brightness = min(100, self.brightness + amount)
        print(f"[{self.name}] Brightness increased to {self.brightness}%")

    def decrease_brightness(self, amount=10):
        if self.power_status == "OFF":
            print(f"Cannot adjust brightness. [{self.name}] is OFF.")
            return

        self.brightness = max(0, self.brightness - amount)
        print(f"[{self.name}] Brightness decreased to {self.brightness}%")

    def display_info(self):
        super().display_info()
        print(f"Brightness: {self.brightness}%")


class SecurityCamera(SmartDevice):
    def __init__(self, device_id, name):
        super().__init__(device_id, name)
        self.recording_status = "NOT RECORDING"

    def start_recording(self):
        if self.power_status == "OFF":
            print(f"Cannot start recording. [{self.name}] is OFF.")
            return

        if self.recording_status == "RECORDING":
            print(f"[{self.name}] is already recording.")
            return

        self.recording_status = "RECORDING"
        print(f"[{self.name}] has started recording video.")

    def stop_recording(self):
        if self.recording_status == "RECORDING":
            self.recording_status = "NOT RECORDING"
            print(f"[{self.name}] has stopped recording.")
        else:
            print(f"[{self.name}] is not recording.")

    def turn_off(self):
        if self.recording_status == "RECORDING":
            self.recording_status = "NOT RECORDING"
            print(f"[{self.name}] recording stopped.")

        super().turn_off()

    def display_info(self):
        super().display_info()
        print(f"Recording Status: {self.recording_status}")
def main():
    sensor = TemperatureSensor("TEMP-001", "Living Room Thermometer", 24.0)
    light = SmartLight("LGT-002", "Bedroom Smart Bulb", 75)
    camera = SecurityCamera("CAM-003", "Front Door Camera")

    devices = [sensor, light, camera]

    while True:
        print("\n=== SMART DEVICE MANAGEMENT SYSTEM ===")
        print("1. Display Device Information")
        print("2. Turn Device On")
        print("3. Turn Device Off")
        print("4. Read Temperature")
        print("5. Adjust Brightness")
        print("6. Start/Stop Recording")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            print("\n--- Current Device Registry ---")
            for device in devices:
                device.display_info()
                print("-" * 30)

        elif choice in ["2", "3"]:
            action = "ON" if choice == "2" else "OFF"

            print(f"\nSelect device to turn {action}:")
            for index, device in enumerate(devices, start=1):
                print(f"{index}. {device.name}")

            try:
                selection = int(input("Choice: "))
                if 1 <= selection <= len(devices):
                    device = devices[selection - 1]
                    if action == "ON":
                        device.turn_on()
                    else:
                        device.turn_off()
                else:
                    print("Invalid device selection.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            sensor.read_temperature()

        elif choice == "5":
            print("\n1. Increase Brightness")
            print("2. Decrease Brightness")

            action = input("Choice: ").strip()

            try:
                amount = int(input("Enter amount (0-100): "))

                if amount < 0:
                    print("Brightness value cannot be negative.")
                    continue

                if action == "1":
                    light.increase_brightness(amount)
                elif action == "2":
                    light.decrease_brightness(amount)
                else:
                    print("Invalid option.")

            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "6":
            print("\n1. Start Recording")
            print("2. Stop Recording")

            action = input("Choice: ").strip()

            if action == "1":
                camera.start_recording()
            elif action == "2":
                camera.stop_recording()
            else:
                print("Invalid option.")

        elif choice == "7":
            print("\nThank you for using the Smart Device Management System.")
            print("Goodbye!")
            break

        else:
            print("Invalid menu option. Please try again.")


if __name__ == "__main__":
    main()