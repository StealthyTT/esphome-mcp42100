#pragma once

#include "esphome/core/component.h"
#include "esphome/components/spi/spi.h"

namespace esphome {
namespace mcp42100 {

class MCP42100 : public Component {
 public:
  MCP42100() = default;

  void set_spi(spi::SPIComponent *spi) { spi_ = spi; }
  void set_cs_pin(GPIOPin *cs) { cs_ = cs; }

  void setup() override {
    cs_->setup();
    cs_->digital_write(true);
  }

  void dump_config() override {
    ESP_LOGCONFIG("mcp42100", "MCP42100 initialized.");
  }

 protected:
  spi::SPIComponent *spi_;
  GPIOPin *cs_;
};

}  // namespace mcp42100
}  // namespace esphome