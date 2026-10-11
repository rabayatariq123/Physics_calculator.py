#  Physics Formula Calculator (Thermodynamics + Heat + Energy)
# Each formula is selectable by number. Now with main menu loop.

def physics_calculator():
    import math
    while True:
        print("\n PHYSICS FORMULA CALCULATOR ")
        print("""
Choose a formula:
1. Q = m * c * ΔT              (Sensible Heat)
2. Q = m * L                   (Latent Heat)
3. PV = nRT                    (Ideal Gas Law)
4. Q = m * Lf                  (Latent Heat of Fusion)
5. Q = m * Lv                  (Latent Heat of Vaporization)
6. ΔV = β * V * ΔT             (Thermal Expansion - Volume)
7. σ = α * E * ΔT              (Thermal Stress)
8. W = P * ΔV                  (Work done by gas)
9. η = (W_out / Q_in) * 100    (Efficiency)
10. P = F / A                  (Pressure)
11. W = F * d * cosθ           (Work done)
12. U = (3/2) * n * R * T      (Internal Energy of Ideal Gas)
13. Cp - Cv = R                (Mayer’s Relation)
14. γ = Cp / Cv                (Adiabatic Index)
15. PV^γ = Constant            (Adiabatic Process)
16. Q = I * V * t              (Electrical Heat Energy)
17. P = W / t                  (Power)
18. ΔL = α * L * ΔT            (Linear Expansion)
19. ΔA = 2α * A * ΔT           (Area Expansion)
20. E = Q / t                  (Rate of Heat Flow)
21. Exit
""")
        choice = input("Enter formula number (1–21): ")

        #  1. Sensible Heat
        if choice == '1':
            m = float(input("Enter mass (kg): "))
            c = float(input("Enter specific heat (J/kg°C): "))
            dT = float(input("Enter change in temperature (°C): "))
            Q = m * c * dT
            print("Heat (Q) =", Q, "Joules")

        # 2. Latent Heat
        elif choice == '2':
            m = float(input("Enter mass (kg): "))
            L = float(input("Enter latent heat (J/kg): "))
            Q = m * L
            print("Heat (Q) =", Q, "Joules")

        #  3. Ideal Gas Law
        elif choice == '3':
            n = float(input("Enter moles of gas: "))
            R = 8.314
            T = float(input("Enter temperature (K): "))
            P = float(input("Enter pressure (Pa): "))
            V = (n * R * T) / P
            print("Volume (V) =", V, "m³")

        #  4. Latent Heat of Fusion
        elif choice == '4':
            m = float(input("Enter mass (kg): "))
            Lf = float(input("Enter latent heat of fusion (J/kg): "))
            Q = m * Lf
            print("Heat required for fusion =", Q, "Joules")

        #  5. Latent Heat of Vaporization
        elif choice == '5':
            m = float(input("Enter mass (kg): "))
            Lv = float(input("Enter latent heat of vaporization (J/kg): "))
            Q = m * Lv
            print("Heat required for vaporization =", Q, "Joules")

        # 6. Thermal Expansion (Volume)
        elif choice == '6':
            beta = float(input("Enter coefficient of volumetric expansion: "))
            V = float(input("Enter original volume (m³): "))
            dT = float(input("Enter temperature change (°C): "))
            dV = beta * V * dT
            print("Change in Volume (ΔV) =", dV, "m³")

        #  7. Thermal Stress
        elif choice == '7':
            alpha = float(input("Enter coefficient of linear expansion: "))
            E = float(input("Enter Young's modulus (Pa): "))
            dT = float(input("Enter temperature change (°C): "))
            sigma = alpha * E * dT
            print("Thermal Stress (σ) =", sigma, "Pa")

        #  8. Work done by gas
        elif choice == '8':
            P = float(input("Enter pressure (Pa): "))
            dV = float(input("Enter change in volume (m³): "))
            W = P * dV
            print("Work done (W) =", W, "Joules")

        #  9. Efficiency
        elif choice == '9':
            W_out = float(input("Enter work output (J): "))
            Q_in = float(input("Enter heat input (J): "))
            efficiency = (W_out / Q_in) * 100
            print("Efficiency =", efficiency, "%")

        # 10. Pressure
        elif choice == '10':
            F = float(input("Enter force (N): "))
            A = float(input("Enter area (m²): "))
            P = F / A
            print("Pressure =", P, "Pa")

        #  11. Work Done
        elif choice == '11':
            F = float(input("Enter force (N): "))
            d = float(input("Enter distance (m): "))
            theta = float(input("Enter angle (degrees): "))
            W = F * d * math.cos(math.radians(theta))
            print("Work Done =", W, "Joules")

        # 12. Internal Energy
        elif choice == '12':
            n = float(input("Enter number of moles: "))
            R = 8.314
            T = float(input("Enter temperature (K): "))
            U = 1.5 * n * R * T
            print("Internal Energy (U) =", U, "Joules")

        #  13. Mayer’s Relation
        elif choice == '13':
            R = 8.314
            print("Cp - Cv = R =", R)

        # 14. Adiabatic Index
        elif choice == '14':
            Cp = float(input("Enter Cp: "))
            Cv = float(input("Enter Cv: "))
            gamma = Cp / Cv
            print("Adiabatic Index (γ) =", gamma)

        #  15. Adiabatic Process
        elif choice == '15':
            print("For adiabatic process: PV^γ = constant")
            print("No numeric computation needed.")

        # 16. Electrical Heat Energy
        elif choice == '16':
            I = float(input("Enter current (A): "))
            V = float(input("Enter voltage (V): "))
            t = float(input("Enter time (s): "))
            Q = I * V * t
            print("Heat Energy (Q) =", Q, "Joules")

        #  17. Power
        elif choice == '17':
            W = float(input("Enter work done (J): "))
            t = float(input("Enter time (s): "))
            P = W / t
            print("Power (P) =", P, "Watts")

        #  18. Linear Expansion
        elif choice == '18':
            alpha = float(input("Enter coefficient of linear expansion: "))
            L = float(input("Enter original length (m): "))
            dT = float(input("Enter temperature change (°C): "))
            dL = alpha * L * dT
            print("Change in Length (ΔL) =", dL, "m")

        # 19. Area Expansion
        elif choice == '19':
            alpha = float(input("Enter coefficient of linear expansion: "))
            A = float(input("Enter original area (m²): "))
            dT = float(input("Enter temperature change (°C): "))
            dA = 2 * alpha * A * dT
            print("Change in Area (ΔA) =", dA, "m²")

        #  20. Rate of Heat Flow
        elif choice == '20':
            Q = float(input("Enter total heat transferred (J): "))
            t = float(input("Enter time (s): "))
            rate = Q / t
            print("Rate of Heat Flow (E) =", rate, "J/s")

        # 21. Exit
        elif choice == '21':
            print("Exiting calculator. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 21.")

        input("\nPress Enter to return to the main menu...")
        #pause before looping again

# Run the calculator
physics_calculator()