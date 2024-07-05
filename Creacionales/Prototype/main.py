"""3. Aquí se lleva a cabo la implementación del patrón."""

from concrete_prototype import SystemConfigPrototype

def main():
    config = {
        "OS":"Linux",
        "Version":"Ubuntu 20.04",
    }
    original_config = SystemConfigPrototype(config)
    cloned_config = original_config.clone()
    print("Original config: {}", format(original_config.configuration))
    print("Cloned config: {}", format(cloned_config.configuration))

if __name__ == "__main__":
    main()