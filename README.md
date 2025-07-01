# Paperless-ngx UYAP Parser

This is a custom parser for [paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) designed to handle import of UYAP Editör `.eyp` files ("E-Yazışma Paketi"). That's a weird format used for Turkish formal communications, often when communicating with government or courts.

This parser only supports parsing .eyp files with an embedded pdf at `ustyazi/UstYazi.pdf`.

It merely opens the `.eyp` file (which is a zip file), checks for the existence of that PDF, then passes it to the default paperless-ngx PDF parser.

The original file remains the `.eyp` (and can be downloaded from `paperless-ngx`), but an archived version (which is based on the `.pdf`) is produced as well, which is what gets rendered, OCR'd, thumbnailed, etc.

## Installation

(Taken from [paperless-media](https://github.com/laymance/paperless-media/blob/main/README.md))

You need to make the `paperless_uyap` directory available to your paperless-ngx instance.

### Docker Installation

1.  **Mount the Parser Directory:**
    Mount the `paperless_uyap` directory into the paperless-ngx webserver container's custom script directory (`/usr/src/paperless/src`). Update your `docker-compose.yml` or Docker run command.

    *Example `docker-compose.yml` snippet:*
    ```yaml
    services:
      webserver:
        # ... other webserver config ...
        volumes:
          - /path/to/your/paperless_uyap:/usr/src/paperless/src/paperless_uyap
          # ... other volumes ...
    ```
    Replace `/path/to/your/paperless_uyap` with the actual path to the `paperless_uyap` directory on your host machine.

2.  Set an environment variable telling paperless to load the new extension. This can be done via 
    the docker-compose.yml or by injecting a environment variable in via portainer or another method.  
      
    *Example `docker-compose.yml` snippet:*
    ```yaml
    environment:
        PAPERLESS_APPS: paperless_uyap
    ```

3.  **Restart Paperless-ngx:**
    Restart your paperless-ngx stack:
    ```bash
    docker-compose up -d
    ```

Done! You should be able to upload `.eyp` files now.
