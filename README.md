# Aplicación de Aprendizaje Electrónico

Bienvenido a nuestra aplicación de aprendizaje electrónico. Esta aplicación utiliza FastAPI y PostgreSQL para proporcionar una plataforma de cursos en línea. A continuación, encontrarás instrucciones para levantar la aplicación de dos maneras diferentes: utilizando Docker Compose o directamente sin Docker Compose.

## Levantar la Aplicación con Docker Compose

### Requisitos Previos
- Docker y Docker Compose instalados en tu sistema.

### Pasos
1. Clona este repositorio en tu máquina local:

    ```bash
    git clone https://github.com/kevorojas/e-learning-api.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd aplicacion-aprendizaje-electronico
    ```

3. Copia el archivo de ejemplo `.env.example` y renómbralo a `.env`. Luego, edita el archivo `.env` y proporciona los valores adecuados para las variables de entorno.

4. Ejecuta los contenedores Docker con Docker Compose:

    ```bash
    docker-compose up -d --build
    ```

5. La aplicación estará disponible en `http://localhost:8000`.

6. Puedes encontrar la documentación de la API en `http://localhost:8000/docs`.

## Levantar la Aplicación sin Docker Compose

### Requisitos Previos
- Python instalado en tu sistema.
- Una instancia de PostgreSQL configurada y accesible.

### Pasos
1. Clona este repositorio en tu máquina local:

    ```bash
    git clone https://github.com/kevorojas/e-learning-api.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd aplicacion-aprendizaje-electronico
    ```

3. Copia el archivo de ejemplo `.env.example` y renómbralo a `.env`. Luego, edita el archivo `.env` y proporciona los valores adecuados para las variables de entorno, especialmente la conexión a la base de datos PostgreSQL.

4. Instala las dependencias de Python:

    ```bash
    pip install -r requirements.txt
    ```

5. Inicia la aplicación:

    ```bash
    uvicorn main:app --reload
    ```

6. La aplicación estará disponible en `http://localhost:8000`.

7. Puedes encontrar la documentación de la API en `http://localhost:8000/docs`.

## Variables de Entorno

Asegúrate de configurar las siguientes variables de entorno en el archivo `.env`:

- `DATABASE_URL`: La URL de conexión a la base de datos PostgreSQL.
- Otras variables específicas según las necesidades de tu aplicación.

---

Esperamos que disfrutes utilizando nuestra aplicación de aprendizaje electrónico. Si tienes alguna pregunta o encuentras algún problema, no dudes en contactarnos.
