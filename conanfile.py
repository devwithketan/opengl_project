from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain,CMakeDeps
import os
from conan.tools.files import copy

class OpenGLApp(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    #generators = "CMakeToolchain", "CMakeDeps"

    def requirements(self):
        self.requires("glfw/3.4")

    def build_requirements(self):
        self.tool_requires("cmake/3.22.6")
    
    def generate(self):
        tc = CMakeToolchain(self)
        deps = CMakeDeps(self)
        deps.generate()
        tc.generate()
        
    
        # copy(self, "*glfw*", os.path.join(self.dependencies["imgui"].package_folder,
            # "res", "bindings"), os.path.join(self.source_folder, "bindings"))
        # copy(self, "*opengl3*", os.path.join(self.dependencies["imgui"].package_folder,
            # "res", "bindings"), os.path.join(self.source_folder, "bindings"))
    
    def layout(self):
        # We make the assumption that if the compiler is msvc the
        # CMake generator is multi-config
        multi = True if self.settings.get_safe("compiler") == "msvc" else False
        if multi:
            self.folders.generators = os.path.join("build", "generators")
            self.folders.build = "build"
        else:
            self.folders.generators = os.path.join("build", str(self.settings.build_type), "generators")
            self.folders.build = os.path.join("build", str(self.settings.build_type))
            
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
    
    