# Sistema de Clasificación y Recolección de Datos

Este proyecto implementa un sistema de microservicios para la clasificación de data centers partners y la recolección de datos médicos. La solución está diseñada siguiendo los principios de **# Domain-Driven Design (DDD)** y **Arquitectura Hexagonal (Ports and Adapters)**, garantizando escalabilidad y mantenibilidad.

## Características principales

- **Microservicios desacoplados** organizados en contenedores Docker.
- **Comunicación asíncrona** mediante Apache Pulsar.
- **Bases de datos MySQL** separadas para operaciones de comando y consulta.
- **Arquitectura modular** basada en DDD y Hexagonal Architecture.

## Componentes del sistema

El sistema está distribuido en varios microservicios, cada uno con una responsabilidad específica:

- `data_center_classifier` - Clasificación de data centers partners.
- `collector_command` - Procesamiento y recolección de datos médicos.
- `collector_query` - Consulta de datos recolectados.
- `db_command` y `db_query` - Bases de datos MySQL para almacenamiento de datos recolectados.
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
├── data_center_classifier/ # Microservicio de clasificación de data centers
│   ├── application/
│   │   ├── __init__.py
│   │   └── service_raw_data.py # Servicio de procesamiento de datos sin procesar
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── model_raw_data.py # Modelo de datos sin procesar
│   │   └── port_collector.py # Puerto para la recolección
│   ├── infrastructure/
│   │   ├── http/
│   │   ├── pulsar/
│   │   └── __init__.py
│   ├── venv/ # Entorno virtual
│   ├── Dockerfile # Definición del contenedor
│   ├── main.py # Punto de entrada
│   └── requirements.txt # Dependencias Python
│
├── collector_command/ # Microservicio de recolección (Comando)
│   ├── application/
│   │   ├── __init__.py
│   │   ├── dto_raw_data.py # DTO para datos sin procesar
│   │   └── service_collector_cmd.py # Servicio de recolección de comandos
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── model_collected_data.py # Modelo de datos recolectados
│   │   ├── port_collector_query.py # Puerto de consulta de recolección
│   │   └── port_collector_repo.py # Repositorio de recolección
│   ├── infrastructure/
│   │   ├── db/ # Base de datos
│   │   ├── pulsar/ # Mensajería Apache Pulsar
│   │   └── __init__.py
│   ├── venv/ # Entorno virtual
│   └── main.py # Punto de entrada
│
├── collector_query/ # Microservicio de consulta de recolección
│   ├── application/
│   │   ├── __init__.py
│   │   ├── dto_raw_data.py # DTO para datos sin procesar
│   │   └── service_collector_query.py # Servicio de consulta de recolección
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── model_collected_data.py # Modelo de datos recolectados
│   │   └── port_collector_repo.py # Puerto del repositorio de recolección
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

- **`collector_command`**: Responsable de procesar y recolectar los datos médicos, manejando las operaciones de escritura.
- **`collector_query`**: Encargado de gestionar las consultas a los datos recolectados, optimizando las operaciones de lectura.

Además, se utiliza **Event Sourcing** para almacenar el historial de eventos en Apache Pulsar, asegurando la trazabilidad de los cambios en los datos médicos recolectados.

### Topología de Bases de Datos

El sistema se ha planteado de forma descentralizada, donde cada microservicio cuenta con su propia base de datos para mejorar el rendimiento y la escalabilidad:

- **`db_command`**: Base de datos utilizada para almacenar datos en proceso de recolección. Pertenece al microservicio **`collector_command`**.
- **`db_query`**: Base de datos optimizada para la consulta de datos recolectados. Pertenece al microservicio **`collector_query`**.

### Arquitectura Hexagonal (Ports and Adapters)

- **Puertos y Adaptadores:**
  - La lógica central se comunica a través de puertos (interfaces) con adaptadores de entrada y salida.

- **Adaptadores de Entrada:**
  - `collector_command` y `data_center_classifier` procesan peticiones y las dirigen a los casos de uso.

- **Adaptadores de Salida:**
  - Persistencia en MySQL y mensajería con Apache Pulsar.

## Notas Adicionales

- Se requiere tener Docker instalado en tu sistema.
- Configurar las variables de entorno en `docker-compose.yml`.
