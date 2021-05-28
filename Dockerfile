FROM homeassistant/home-assistant:latest

RUN mkdir custom_components

COPY custom_components /config/custom_components
COPY configuration.yaml /config