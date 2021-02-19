class Swift:
    def start(self):
        print(" SWIFT STARTED")
    def accelerate(self):
        print(" SWIFT ACCELERATED")
    def stop(self):
        print(" SWIFT STOPPED")
class Seltos:
    def start(self):
        print(" SELTOS STARTED")
    def accelerate(self):
        print(" SELTOS ACCELERATED")
    def stop(self):
        print(" SELTOS STOPPED")
class Drive:
    def drv(self,car):
        car.start()
        car.stop()
        car.stop()
obj=Swift()
drive=Drive()
drive.drv(obj)
