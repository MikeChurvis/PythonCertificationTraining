class StopPacking(Exception):
    def __init__(self, processor_id):
        self.raised_by = processor_id

    def __str__(self):
        return f'Packing stopped by processor {self.raised_by}'


class ApplePackagingMonitor:
    __processor_serial_number = 1
    apples_processed = 0
    total_weight_processed = 0
    max_allowed_weight_processed = 300

    def __init__(self):
        self.processor_id = ApplePackagingMonitor.__processor_serial_number
        ApplePackagingMonitor.__processor_serial_number += 1

    def process_apple(self, weight):
        if ApplePackagingMonitor.total_weight_processed + weight > ApplePackagingMonitor.max_allowed_weight_processed:
            raise StopPacking(self.processor_id)

        ApplePackagingMonitor.total_weight_processed += weight
        ApplePackagingMonitor.apples_processed += 1


if __name__ == '__main__':
    import random


    def main():
        apple_min_weight = 0.2
        apple_max_weight = 0.5
        processor1 = ApplePackagingMonitor()
        processor2 = ApplePackagingMonitor()

        while True:
            try:
                processor1.process_apple(random.uniform(apple_min_weight, apple_max_weight))
                processor2.process_apple(random.uniform(apple_min_weight, apple_max_weight))
            except StopPacking as stop_signal:
                print(stop_signal)
                break

        print(f'Applies processed: {ApplePackagingMonitor.apples_processed}')
        print(f'Total weight processed: {ApplePackagingMonitor.total_weight_processed}')


    main()
