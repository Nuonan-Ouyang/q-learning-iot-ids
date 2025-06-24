import time

def read_temp():
    with open("/sys/class/thermal/thermal_zone0/temp") as f:
        return int(f.read()) / 1000.0

def main():
    while True:
        temp = read_temp()
        print(f"CPU Temperature: {temp}°C")
        time.sleep(5)

if __name__ == "__main__":
    main()
