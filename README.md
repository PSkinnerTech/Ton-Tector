# Ton-Tector

![Ton-Tector Device](./TON-Tector/img/ton-tector1.jpeg)

Ton-Tector is a revolutionary device combining blockchain technology with environmental monitoring. Designed to function as a lightweight node in The Open Network (TON) blockchain, Ton-Tector also serves as an early detection system for natural disasters. Equipped with sensors for temperature and seismic activity, it provides real-time alerts to users via a Telegram mini-app. This open-source project aims to provide accessible and reliable technology for safety and blockchain integration.

## Quick Links
- [Hardware Specifications](./HardwareSpecs.md)
- [Software Specifications](./SoftwareSpecs.md)

## Who I Am

My name is Patrick Skinner, and I'm the Lead DevRel for Forward Research | Arweave. I bring my experience as a former Paratrooper Medic to my work, driven by a passion for building blockchain technology that provides tangible benefits in real-world situations. I am dedicated to developing solutions that can truly help those in need, especially in critical scenarios. You can follow my work and updates on [GitHub](https://github.com/PSkinnerTech), [X](https://x.com/PSkinnerTech), and visit my website at [patrickskinner.tech](https://patrickskinner.tech/).

## Open Source

Ton-Tector is an open-source project designed to encourage community collaboration and innovation. We welcome contributions from developers and enthusiasts alike to help improve and expand the capabilities of this project. By leveraging the collective expertise of the community, we aim to create a robust and reliable system for monitoring environmental conditions and issuing timely alerts. Your contributions can make a real difference in advancing this technology.

## License

This project is licensed under the MIT License, allowing for open use, modification, and distribution. This permissive license ensures that Ton-Tector remains accessible to everyone, fostering a spirit of collaboration and continuous improvement. For more details, please refer to the LICENSE file in the project's repository.

sudo qemu-system-arm \
    -kernel $(pwd)/qemu-rpi-kernel/kernel-qemu-4.19.50-buster \
    -cpu arm1176 \
    -m 256 \
    -M versatilepb \
    -dtb $(pwd)/qemu-rpi-kernel/versatile-pb.dtb \
    -no-reboot \
    -serial stdio \
    -append "root=/dev/sda2 rootfstype=ext4 rw init=/bin/bash" \
    -drive file=/Users/pskinnertech/Downloads/2024-07-04-raspios-bullseye-armhf-lite.img,format=raw \
    -net nic -net user,hostfwd=tcp::5022-:22

    