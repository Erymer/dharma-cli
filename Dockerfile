FROM archlinux:latest


LABEL maintainer="Erymer"

ENV PYTHONUNBUFFERED 1

COPY . /dharma
WORKDIR /dharma


RUN useradd --create-home -p "" dharma && \
    chown -R dharma /dharma && \
    echo 'root:0000' | chpasswd && \
    pacman -Syu --noconfirm && \
    pacman -S --noconfirm python python-pytest python-installer \
                          python-build python-setuptools && \
    python -m build && \
    python -m installer dist/*.whl



ENV PATH="/py/bin:$PATH"

USER dharma
