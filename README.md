# LLM Coding Agent

## Description

This project features a coding_agent that uses the Gemini API to interact with the file system. It enables users to perform a variety of operations, including listing files and directories, reading file content, writing or overwriting files, and executing Python code. Guided by a structured prompt and a suite of predefined functions, the agent is designed to automate coding tasks and offers a convenient, programmatic approach to file management.

## Functionalities

- List files in specified folder
- Read the files of directory
- Execute python code
- Write files

## How to use
1. Clone the repo:

```bash
git clone git@github.com:luis-octavius/llm-agent.git 
cd llm-agent 
```
  
  
> [!WARNING]
> Originally, the directory used by the agent is `llm-agent/archives`, so, if you want to use in another folder you have to change the constant variable in the config file.    
  
  
2. Execute:

```bash 
uv run main.py "<your_prompt_here>" --verbose # the --verbose flag is optional
```

## Requirements
- uv 
- Python 3.2
- Gemini API Key
 
