\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  2 pax_12 + 2 pax_23 + 5 pax_31 - 2 x_12 - 5 x_23 - 5 x_31 - 10 nt_12
   - 10 nt_23 - 10 nt_31 - 2 nv_12 - 2 nv_23 - 2 nv_31
Subject To
 max_tubes_12: - 2 x_12 + nt_12 <= 0
 max_tubes_23: - 2 x_23 + nt_23 <= 0
 max_tubes_31: - 2 x_31 + nt_31 <= 0
 max_vehicles_12: - nt_12 + nv_12 <= 0
 max_vehicles_23: - nt_23 + nv_23 <= 0
 max_vehicles_31: - nt_31 + nv_31 <= 0
 max_passengers12: pax_12 - 5 nv_12 <= 0
 max_passengers23: pax_23 - 5 nv_23 <= 0
 max_passengers31: pax_31 - 5 nv_31 <= 0
Bounds
 pax_12 <= 5
 pax_23 <= 10
 pax_31 <= 15
Binaries
 x_12 x_23 x_31
Generals
 pax_12 pax_23 pax_31 nt_12 nt_23 nt_31 nv_12 nv_23 nv_31
End
