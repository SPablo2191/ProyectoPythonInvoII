import random
import queue # queuelib
from Customer import Customer



def simulate_md1(lambd, mu, max_time, verbosity=0):
    md1 = queue.Queue()
    served_customers = []
    unserved_customers = []
    next_arrival = random.expovariate(lambd)
    next_service = next_arrival + 1/mu

    
    t = next_arrival

    # cantidad de cliente
    cid = 1

    while t < max_time:

        if t == next_arrival:
            customer = Customer(cid, arrival_time=t)
            cid += 1
            md1.put(customer)

            if verbosity >= 2:
                print("{:10.2f}: Cliente # {} Llega".format(t, customer.cid))

            next_arrival = t + random.expovariate(lambd)

        # El cliente en la cabeza de la cola es atendido
        if t == next_service:
            done_customer = md1.get()
            done_customer.departure_time = t

            served_customers.append(done_customer)

            if verbosity >= 2:
                print("{:10.2f}: Cliente # {} se va".format(
                    t, done_customer.cid))

            if md1.empty():
                next_service = next_arrival + 1/mu
            else:
                next_service = t + 1/mu

        if verbosity >= 1:
            print("{:10.2f}: {}".format(t, "#"*md1.qsize()))

        t = min(next_arrival, next_service)

   
    while not md1.empty():
        unserved_customers.append(md1.get())

    return served_customers, unserved_customers


vec1, vec2 = simulate_md1(1, 1, 100, verbosity=2)
print(f"clientes servidos: {vec1}")
print(f"clientes en espera: {vec2}")
