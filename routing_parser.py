# routing_parser.py

def clean_routing(routing_str):
    """Convert BKK-DMK-HKT into uppercase no dash format: BKKDMKHKT"""
    return routing_str.replace("-", "").upper()

def is_valid_routing(routing, valid_airports):
    """Check if all segments in routing are known airports"""
    segments = routing.upper().split("-")
    return all(seg in valid_airports for seg in segments)

# Example usage
if __name__ == "__main__":
    routing = "BKK-DMK-HKT"
    airports = ["BKK", "DMK", "HKT", "CNX", "KBV"]
    print("Cleaned:", clean_routing(routing))
    print("Valid?", is_valid_routing(routing, airports))
