# Sistema de Clasificación y Tokenización de Datos

Este proyecto implementa un sistema de microservicios para la clasificación de modelos de IA y la tokenización de datos médicos. La solución está diseñada siguiendo los principios de **# Domain-Driven Design (DDD)** y **Arquitectura Hexagonal (Ports and Adapters)**, garantizando escalabilidad y mantenibilidad.

## Características principales

- **Microservicios desacoplados** organizados en contenedores Docker.
- **Comunicación asíncrona** mediante Apache Pulsar.
- **Bases de datos MySQL** separadas para operaciones de comando y consulta.
- **Arquitectura modular** basada en DDD y Hexagonal Architecture.

## Componentes del sistema

El sistema está distribuido en varios microservicios, cada uno con una responsabilidad específica:

- `ai_model_classifier` - Clasificación de modelos de IA.
- `tokenizer_command` - Procesamiento y tokenización de datos médicos.
- `tokenizer_query` - Consulta de datos tokenizados.
- `db_command` y `db_query` - Bases de datos MySQL para almacenamiento de datos tokenizados.
- `apache_pulsar` - Gestor de eventos para la comunicación entre microservicios.

## Instalación y Ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Iniciar los servicios con Docker Compose

```bash
docker-compose up --build
```

Esto iniciará todos los microservicios y bases de datos definidas en `docker-compose.yml`.

## Estructura del Proyecto

```plaintext
rendimiento/
├── ai_model_classifier/ # Microservicio de clasificación de modelos
│   ├── application/
│   │   ├── __init__.py
│   │   └── service_raw_data.py # Servicio de procesamiento de datos sin procesar
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── model_raw_data.py # Modelo de datos sin procesar
│   │   └── port_tokenizer.py # Puerto para la tokenización
│   ├── infrastructure/
│   │   ├── http/
│   │   ├── pulsar/
│   │   └── __init__.py
│   ├── venv/ # Entorno virtual
│   ├── Dockerfile # Definición del contenedor
│   ├── main.py # Punto de entrada
│   └── requirements.txt # Dependencias Python
│
├── tokenizer_command/ # Microservicio de tokenización (Comando)
│   ├── application/
│   │   ├── __init__.py
│   │   ├── dto_raw_data.py # DTO para datos sin procesar
│   │   └── service_tokenizer_cmd.py # Servicio de tokenización de comandos
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── model_tokenized_data.py # Modelo de datos tokenizados
│   │   ├── port_tokenizer_query.py # Puerto de consulta de tokenización
│   │   └── port_tokenizer_repo.py # Repositorio de tokenización
│   ├── infrastructure/
│   │   ├── db/ # Base de datos
│   │   ├── pulsar/ # Mensajería Apache Pulsar
│   │   └── __init__.py
│   ├── venv/ # Entorno virtual
│   └── main.py # Punto de entrada
│
├── tokenizer_query/ # Microservicio de consulta de tokenización
│   ├── application/
│   │   ├── __init__.py
│   │   ├── dto_raw_data.py # DTO para datos sin procesar
│   │   └── service_tokenizer_query.py # Servicio de consulta de tokenización
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── model_tokenized_data.py # Modelo de datos tokenizados
│   │   └── port_tokenizer_repo.py # Puerto del repositorio de tokenización
│   ├── infrastructure/
│   │   ├── db/ # Base de datos
│   │   ├── http/ # API HTTP
│   │   ├── pulsar/ # Mensajería Apache Pulsar
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── main.py # Punto de entrada del microservicio
│
├── z_test/ # Pruebas de carga y estrés
│   ├── locust_stress_test.py # Pruebas de estrés con Locust
│   └── __init__.py
```

## Arquitectura del Sistema

### CQRS y Event Sourcing

Este sistema implementa **CQRS (Command Query Responsibility Segregation)** para separar claramente las operaciones de escritura y lectura, mejorando la escalabilidad y el rendimiento. Se tienen dos microservicios especializados para esta separación:

- **`tokenizer_command`**: Responsable de procesar y tokenizar los datos médicos, manejando las operaciones de escritura.
- **`tokenizer_query`**: Encargado de gestionar las consultas a los datos tokenizados, optimizando las operaciones de lectura.

Además, se utiliza **Event Sourcing** para almacenar el historial de eventos en Apache Pulsar, asegurando la trazabilidad de los cambios en los datos médicos tokenizados.

### Topología de Bases de Datos

El sistema se ha planteado de forma descentralizada, donde cada microservicio cuenta con su propia base de datos para mejorar el rendimiento y la escalabilidad:

- **`db_command`**: Base de datos utilizada para almacenar datos en proceso de tokenización. Pertenece al microservicio **`tokenizer_command`**.
- **`db_query`**: Base de datos optimizada para la consulta de datos tokenizados. Pertenece al microservicio **`tokenizer_query`**.

Cada microservicio accede exclusivamente a su base de datos correspondiente según su responsabilidad dentro del patrón CQRS, asegurando una mejor distribución de carga y evitando bloqueos innecesarios.



### Domain-Driven Design (DDD)

- **Modelo de Dominio:**

  - Representa datos médicos y sus transformaciones mediante DTOs como `MedicalRecordDTO`.

- **Casos de Uso:**

  - La lógica de negocio se encapsula en `TokenizerCmdService`, implementando `ITokenizerCmdService`.

- **Separación de infraestructura:**

  - Se definen interfaces como `ITokenizerRepository` y `ITokenizerQueryPort`, permitiendo desacoplar la persistencia del dominio.

### Arquitectura Hexagonal (Ports and Adapters)

- **Puertos y Adaptadores:**

  - La lógica central se comunica a través de puertos (interfaces) con adaptadores de entrada y salida.

- **Adaptadores de Entrada:**

  - `tokenizer_command` y `ai_model_classifier` procesan peticiones y las dirigen a los casos de uso.

- **Adaptadores de Salida:**

  - Persistencia en MySQL y mensajería con Apache Pulsar.

## Ejecución y Comunicación entre Microservicios

1. **Servicio de Clasificación de Modelos:**

   - Ejecutar `python main.py` en `ai_model_classifier/`.

2. **Servicio de Tokenización (Command):**

   - Consume mensajes de Apache Pulsar, los procesa y tokeniza los datos médicos.

3. **Servicio de Consulta:**

   - Gestiona peticiones sobre datos tokenizados almacenados en `db_query`.

4. **Bases de Datos:**

   - `db_command`: Almacena datos en proceso de tokenización.
   - `db_query`: Almacena datos tokenizados listos para consulta.

## Notas Adicionales

- Se requiere tener Docker instalado en tu sistema.
- Configurar las variables de entorno en `docker-compose.yml`.
