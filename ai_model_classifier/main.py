from infrastructure.http.server import Server
from infrastructure.http.routes import Routes
from application.RawDataService import RawDataService

if __name__ == "__main__":
    raw_data_service = RawDataService()

    router = Routes(raw_data_service).router
    server = Server([router])

    # Run the server
    server.run(host="0.0.0.0", port=8000)