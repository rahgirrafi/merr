#ifndef RPI_MOTOR_CONTROL_HPP
#define RPI_MOTOR_CONTROL_HPP
#include <pigpio.h>
#include <iostream>
#include <fmt/core.h>
#include <chrono>
#include <thread>
#include <signal.h>
#include <cmath>

//use raspberry pi 5 to read encoder pulses and send pwm singals

class RpiMotorControl{
    public:

    int left_motor_pwm_pin;
    int left_motor_enc_pin;
    int right_motor_pwm_pin;
    int right_motor_enc_pin;

    RpiMotorControl() = default;

    RpiMotorControl(int left_motor_pwm_pin, int left_motor_enc_pin, int right_motor_pwm_pin, int right_motor_enc_pin){
        this->left_motor_pwm_pin = left_motor_pwm_pin;
        this->left_motor_enc_pin = left_motor_enc_pin;
        this->right_motor_pwm_pin = right_motor_pwm_pin;
        this->right_motor_enc_pin = right_motor_enc_pin;
    }

    void setup(){
        if (gpioInitialise() < 0)
        {
            std::cout << "pigpio initialisation failed." << std::endl;
        }
        else
        {
            std::cout << "pigpio initialised okay." << std::endl;
        }

        gpioSetMode(left_motor_pwm_pin, PI_OUTPUT);
        gpioSetMode(right_motor_pwm_pin, PI_OUTPUT);

        gpioSetMode(left_motor_enc_pin, PI_INPUT);
        gpioSetMode(right_motor_enc_pin, PI_INPUT);
    }

    void set_pwm(int pwm_pin, int pwm_value){
        gpioPWM(pwm_pin, pwm_value);
    }

};

#endif //RPI_MOTOR_CONTROL_HPP