```
# Use Miniconda as the base image
FROM continuumio/miniconda3:latest

# Set working directory
WORKDIR /app

# Copy Conda environment file
COPY environment.yml /app/environment.yml

# Install Conda environment
RUN conda env create -f environment.yml && conda clean --all -y

# Set environment path
SHELL ["/bin/bash", "-c"]
RUN echo "conda activate dataengineering_env" >> ~/.bashrc
ENV PATH="/opt/conda/envs/dataengineering_env/bin:$PATH"

# Install Jupyter and Notebook
RUN pip install jupyter jupyterlab notebook

# Configure Jupyter to disable authentication
RUN mkdir -p /root/.jupyter && \
    echo "c.ServerApp.password = ''" >> /root/.jupyter/jupyter_server_config.py && \
    echo "c.ServerApp.token = ''" >> /root/.jupyter/jupyter_server_config.py && \
    echo "c.ServerApp.disable_check_xsrf = True" >> /root/.jupyter/jupyter_server_config.py && \
    echo "c.ServerApp.allow_origin = '*'" >> /root/.jupyter/jupyter_server_config.py && \
    echo "c.ServerApp.allow_remote_access = True" >> /root/.jupyter/jupyter_server_config.py

# Expose Jupyter Notebook port
EXPOSE 8888

SHELL ["/bin/bash", "-c"]

# Ensure Conda activates the environment on container start
RUN echo "conda activate dataengineering_env" >> ~/.bashrc
ENV PATH="/opt/conda/envs/dataengineering_env/bin:$PATH"


# Start JupyterLab when the container runs
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--config=/root/.jupyter/jupyter_server_config.py"]

```
