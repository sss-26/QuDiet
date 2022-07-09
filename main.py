from core.quantum_circuit import QuantumCircuit

qc = QuantumCircuit(qregs=(3, 3), init_states=[2, 3, 4])

qc.h(qreg=0, dims=3)
qc.z(qreg=1, dims=3)
qc.x(qreg=2, dims=3)
qc.x(qreg=0, dims=3)
qc.h(qreg=1, dims=3)
qc.z(qreg=2, dims=3)
# qc.cx(acting_on=(0, 2), plus=4, dims=3)

print(qc.exec())