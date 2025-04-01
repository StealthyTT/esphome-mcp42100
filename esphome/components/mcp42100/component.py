import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID, CONF_CS_PIN
from esphome.components import spi

CODEOWNERS = ["@stealthytt"]
DEPENDENCIES = ["spi"]

mcp42100_ns = cg.esphome_ns.namespace("mcp42100")
MCP42100 = mcp42100_ns.class_("MCP42100", cg.Component)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(MCP42100),
    cv.Required(CONF_CS_PIN): cv.pin,
    cv.Required("spi_id"): cv.use_id(spi.SPIComponent),
}).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)

    cs = await cg.gpio_pin_expression(config[CONF_CS_PIN])
    cg.add(var.set_cs_pin(cs))

    spi_ = await cg.get_variable(config["spi_id"])
    cg.add(var.set_spi(spi_))