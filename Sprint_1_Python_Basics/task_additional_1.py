types = {
    1: "Блокирующий",
    2: "Критический",
    3: "Значительный",
    4: "Незначительный",
    5: "Тривиальный",
}

tickets = {
    1: ["API_45", "API_76", "E2E_4"],
    2: ["UI_19", "API_65", "API_76", "E2E_45"],
    3: ["E2E_45", "API_45", "E2E_2"],
    4: ["E2E_9", "API_76"],
    5: ["E2E_2", "API_61"],
}


def unique_tickets_filter(tickets):

    unique_tickets = set()
    ticket_list = [
        (key, ticket) for key, values in tickets.items() for ticket in values
    ]
    new_tickets = {}

    for k, v in ticket_list:
        if v not in unique_tickets:
            unique_tickets.add(v)
            if k not in new_tickets:
                new_tickets[k] = []
            new_tickets[k].append(v)
        else:
            continue

    return new_tickets


def tickets_by_type(types, tickets):
    filtred_tickets = unique_tickets_filter(tickets)
    result = {}
    for k, v in types.items():
        result[v] = filtred_tickets.get(k, [])
    return result


print(tickets_by_type(types, tickets))