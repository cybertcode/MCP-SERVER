from main import api, mcp_app
from fastapi.routing import Mount

with open("routes.txt", "w") as f:
    def print_routes(app, prefix=""):
        f.write(f"--- Routes for prefix: '{prefix}' ---\n")
        for route in app.routes:
            if isinstance(route, Mount):
                f.write(f"Mount: {prefix}{route.path} -> {route.name}\n")
                if hasattr(route, "app"):
                        print_routes(route.app, prefix=prefix + route.path)
            elif hasattr(route, "path"):
                methods = ", ".join(route.methods) if hasattr(route, "methods") else "ALL"
                f.write(f"Route: {prefix}{route.path} [{methods}] -> {route.name}\n")
        f.write(f"--- End Routes for prefix: '{prefix}' ---\n\n")

    f.write("Inspecting api routes:\n")
    print_routes(api)

    f.write("\nInspecting mcp_app routes directly:\n")
    print_routes(mcp_app)
