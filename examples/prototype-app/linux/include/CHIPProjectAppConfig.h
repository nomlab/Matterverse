/*
 *
 *    Copyright (c) 2020 Project CHIP Authors
 *    All rights reserved.
 *
 *    Licensed under the Apache License, Version 2.0 (the "License");
 *    you may not use this file except in compliance with the License.
 *    You may obtain a copy of the License at
 *
 *        http://www.apache.org/licenses/LICENSE-2.0
 *
 *    Unless required by applicable law or agreed to in writing, software
 *    distributed under the License is distributed on an "AS IS" BASIS,
 *    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *    See the License for the specific language governing permissions and
 *    limitations under the License.
 */

#pragma once

// include the CHIPProjectConfig from config/standalone
#include <CHIPProjectConfig.h>

#define CHIP_DEVICE_CONFIG_ENABLE_COMMISSIONER_DISCOVERY 0

// Bulbs do not typically use this - enabled so we can use shell to discover commissioners
#define CHIP_DEVICE_CONFIG_ENABLE_COMMISSIONER_DISCOVERY_CLIENT 1

#define CHIP_DEVICE_CONFIG_ENABLE_EXTENDED_DISCOVERY 1

#define CHIP_DEVICE_CONFIG_ENABLE_COMMISSIONABLE_DEVICE_TYPE 1

#define CHIP_DEVICE_CONFIG_DEVICE_TYPE 0x0015 // Contact sensor

#define CHIP_DEVICE_CONFIG_ENABLE_COMMISSIONABLE_DEVICE_NAME 1

#define CHIP_DEVICE_ENABLE_PORT_PARAMS 1

#define CHIP_DEVICE_CONFIG_DEVICE_NAME "prototype-sensor"

#define CHIP_DEVICE_CONFIG_ENDPOINT_COUNT_PROTOTYPE 1