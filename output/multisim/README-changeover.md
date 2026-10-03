# Multisim simulation package - changeover contacts

`aviation_relay_contactor_changeover_training.cir` is a SPICE netlist for the changeover-contact trainer. Import it into Multisim as a SPICE netlist and run a transient analysis from 0 to 4 seconds.

The model implements the contact counts stated in the component specification:

- KA: four SPDT main contact groups, `a` through `d`.
- KM: three SPDT main contact groups, `a` through `c`.
- Every group transfers from terminal `2-3` (NC) to terminal `1-2` (NO) when its coil energizes.

The default test sequence is:

| Time | State |
|---|---|
| Immediately after source connection | HL_AC1 and HL_DC1 are energized. |
| 0.001 s | S0 closes: HL_AC and HL_DC are energized. |
| 0.8 s | S1 closes: KA and HL_KA energize; KA contacts transfer to 1-2. |
| 1.6 s | S2 closes: KM and HL_KM energize; KM contacts transfer to 1-2. |
| 3.2 s | S1 and S2 open: KA and KM release; contacts return to 2-3. |

For manual maintenance-operation scenarios, edit these sources before importing or rerunning:

- `V_S1CTL`: `DC 5` holds S1 closed; `DC 0` holds it open.
- `V_S2CTL`: `DC 5` holds S2 closed; `DC 0` holds it open.
- `V_Q1CTL` and `V_Q2CTL`: `DC 0` simulates a tripped/open circuit breaker.
- `V_S0CTL`: `DC 0` or `DC 5` opens or closes both S0 poles together.

The occurrence of “2 groups” in the control-logic narrative conflicts with the stated component parameters. This package implements the stated four KA and three KM changeover groups. Contact-current ratings are design annotations; they are not enforced by SPICE.
