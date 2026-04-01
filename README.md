MonitorSys - Portero de infraestructura

Este proyecto es un componente de un ecosistema modular de software. Su función es la supervisión en tiempo real del hardware y disponibilidad de servicios críticos.

## Funcionalidades
- **Monitoreo de Hardware:** Alerta mediante notificación de Telegram si el uso de CPU o RAM supera el 90%.
- **Health Check de Servicios:** Verifica la disponibilidad de la [API-Rest de Precios](https://github.com/MartinEnriqueMendez/api-rest).
- **Notificaciones Instantáneas:** Integración con Telegram Bot API para alertas remotas.

## Arquitectura Modular
Este sistema funciona de manera independiente, sigue una arquitectura de micro-servicios:
1. **Extractor (Scraper):** Genera los datos.
2. **Servidor (API):** Distribuye los datos.
3. **Monitor (Este Repo):** Asegura que todo lo anterior esté online.

## Tecnologias
- Python 3.x
- **psutil:** Gestión de procesos y sistema.
- **requests:** Comunicación con Telegram API.

## Configuración de seguridad
Este proyecto utiliza variables de entorno para proteger las credenciales de telegram
1. Creá un archivo `.env` en la raíz del proyecto.
2. Agregá tus credenciales siguiendo el formato:
    - `TELEGRAM_TOKEN=tu_token`
    - `TELEGRAM_CHAT_ID=tu_id`
3. El archivo `.env` está excluido del repositorio mediante `.gitignore`.
