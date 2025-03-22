from multiprocessing import Process
import http.server as web
import logging
import os


def web_service(server_class=web.HTTPServer, handler_class=web.BaseHTTPRequestHandler):
    """
    We use this because Render requires free web services
    to bind to a port regardless if it's used in the application
    """
    server_address = ("", 10000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


def main(bot_service):
    main_proc = Process(target=bot_service, args=(os.getenv("BOT_TOKEN"),))
    web_proc = Process(target=web_service)

    logger = logging.getLogger(__name__)

    while True:
        try:
            main_proc.start()
            web_proc.start()

            main_proc.join()
            web_proc.join()
        except KeyboardInterrupt:
            logger.warning("Received SIGINT. Terminating processes.")
            if main_proc.is_alive():
                main_proc.terminate()
            if web_proc.is_alive():
                web_proc.terminate()
            break
        except Exception as e:
            logger.error(e)
