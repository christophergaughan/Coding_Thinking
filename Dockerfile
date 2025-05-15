# Use Miniconda as the base image
FROM continuumio/miniconda3:latest

# Set working directory
WORKDIR /app

# Copy Conda environment file
COPY environment.yml /app/environment.yml

# Install Conda environment
RUN conda env create -f environment.yml && conda clean --all -y

# Activate environment and make sure it's on PATH
SHELL ["/bin/bash", "-c"]
ENV PATH="/opt/conda/envs/dataengineering_env/bin:$PATH"
ENV CONDA_DEFAULT_ENV=dataengineering_env

# Install Jupyter and Notebook
RUN pip install jupyter jupyterlab notebook

# Set up Jupyter to allow PyCharm connection (with token, not disabled)
RUN mkdir -p /root/.jupyter && \
    echo "c.ServerApp.ip = '0.0.0.0'" >> /root/.jupyter/jupyter_server_config.py && \
    echo "c.ServerApp.port = 8888" >> /root/.jupyter/jupyter_server_config.py && \
    echo "c.ServerApp.open_browser = False" >> /root/.jupyter/jupyter_server_config.py && \
    echo "c.ServerApp.allow_remote_access = True" >> /root/.jupyter/jupyter_server_config.py

# Expose Jupyter port
EXPOSE 8888

# Launch Jupyter (PyCharm will use the token that gets generated)
CMD ["bash", "-c", "source activate dataengineering_env && jupyter lab --allow-root --config=/root/.jupyter/jupyter_server_config.py"]
