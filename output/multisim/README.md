# Multisim simulation package

`aviation_relay_contactor_training.cir` is a SPICE netlist for the relay/contactor maintenance trainer described in the request. Import it into Multisim as a SPICE netlist, then run a transient analysis from 0 to 4 seconds.

The default test sequence is:

| Time | State |
|---|---|
| 0.001 s | S0 closes: AC and DC power indicators are energized. |
| 0.8 s | S1 closes: KA coil, HL_KA, KA contacts a-d, and KA auxiliary NO contact operate. |
| 1.6 s | S2 closes: KM coil, HL_KM, KM contacts a-c, and KM auxiliary NO contact operate. |
| 3.2 s | S1 and S2 open: KA and KM release; each auxiliary NC contact returns closed. |

For manual maintenance-operation scenarios, edit the following control sources in the netlist before importing or rerunning:

- `V_S1CTL`: use `DC 5` to hold S1 closed, or `DC 0` to hold it open.
- `V_S2CTL`: use `DC 5` to hold S2 closed, or `DC 0` to hold it open.
- `V_Q1CTL` and `V_Q2CTL`: use `DC 0` to simulate a tripped/open circuit breaker.
- `V_S0CTL`: use `DC 0` or `DC 5` to open or close both poles of S0 simultaneously.

The contact models are idealized voltage-controlled switches. They reproduce the requested control and release logic; contact current ratings are design annotations and are not enforced by SPICE.
