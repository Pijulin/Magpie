from conans import ConanFile, CMake

class EffectCommonConan(ConanFile):
	requires = "fmt/8.0.1", "nlohmann_json/3.9.1", "spdlog/1.9.1", "muparser/2.3.2"
	generators = "visual_studio"
	