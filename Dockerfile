FROM archlinux:latest


LABEL maintainer="Erymer"

ENV PYTHONUNBUFFERED 1

COPY . /dharma
VOLUME /dharma
WORKDIR /dharma


RUN useradd --create-home -p "" -G wheel dharma && \
    chown -R dharma /dharma && \
    echo 'root:0000' | chpasswd && \
    pacman -Syu --noconfirm && \
    pacman -S --noconfirm sudo python python-pytest python-installer \
                          python-build python-setuptools base-devel && \
    sed -i 's/# %wheel ALL=(ALL:ALL) NOPASSWD: ALL/%wheel ALL=(ALL:ALL) NOPASSWD: ALL/' /etc/sudoers



ENV PATH="/py/bin:$PATH"

USER dharma
