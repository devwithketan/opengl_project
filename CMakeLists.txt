cmake_minimum_required(VERSION 3.22)

project("OpenGLApp" 
    VERSION 1.0.0
    LANGUAGES C CXX)

# Set C++ standard
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

find_package(glfw3 CONFIG REQUIRED)
#find_package(imgui CONFIG REQUIRED)
#find_package(implot CONFIG REQUIRED)
#find_package(OpenGL REQUIRED)

#add_compile_definitions(NOMINMAX)

# Add the src directory
add_subdirectory(src)

