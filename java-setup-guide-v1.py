import streamlit as st
import os
import subprocess

def check_java_version():
    try:
        result = subprocess.run(["java", "-version"], capture_output=True, text=True, shell=True)
        return result.stderr if result.stderr else result.stdout
    except Exception as e:
        return f"Error checking Java version: {e}"

def main():
    st.set_page_config(page_title="Java Setup Guide", page_icon="☕", layout="centered")
    
    st.title("Java Setup Guide")
    
    st.header("1. Verify Java Installation")
    st.write("To check if Java is installed, open your terminal and run the following command:")
    st.code("java -version", language="sh")
    
    if st.button("Check Java Version"):
        st.code(check_java_version())
    
    st.header("2. Set Up Your Java Project")
    st.write("Create a new directory for your project and navigate into it:")
    st.code("""
mkdir MyJavaProject
cd MyJavaProject
""", language="sh")
    
    st.write("Create a `src` folder inside your project directory:")
    st.code("""
mkdir src
""", language="sh")
    
    st.write("Inside the `src` folder, create a file named `Main.java` with the following content:")
    st.code("""
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
""", language="java")
    
    st.header("3. Compile and Run Your Java Application")
    st.write("Navigate to your project directory and compile the Java source file:")
    st.code("""
javac -d bin src/Main.java
""", language="sh")
    
    st.write("Run the compiled Java program:")
    st.code("""
java -cp bin Main
""", language="sh")
    
    st.write("Expected output:")
    st.code("Hello, World!")
    
    st.header("4. Full Directory Structure")
    st.write("Your project directory should look like this:")
    st.code("""
MyJavaProject
├── src
│   └── Main.java
├── bin
""", language="sh")
    
    st.success("Java setup guide completed! Follow these steps and run your Java program successfully.")
    
    st.header("5. Deploy This Guide on Streamlit")
    st.write("To publish this guide on Streamlit, follow these steps:")
    st.code("""
pip install streamlit
streamlit run app.py
""", language="sh")
    
    st.write("To deploy it on Streamlit Cloud:")
    st.code("""
1. Push your code to GitHub.
2. Go to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Click 'New app' and connect your repository.
4. Deploy your Streamlit app!
""")
    
    st.info("You can now publish and share this guide with others!")

if __name__ == "__main__":
    main()
