# CE spine lock — provisional M09

**Status:** Provisional — human-approved from `brief-merged.md`  
**Code:** `CE`  
**Program:** Comunicación efectiva  
**Client:** Prodensa  
**Size:** `M09` (6 core + 3 complement) — catalog floor is **minimum M08**; shrink may assemble to M08 by dropping complement  
**Evidence mode:** `brief_only`  
**First-ship tier:** `T2`  
**Demo tiers (Prodensa):** `T1` · `T2` · `T3` · `T4` (M01 each, separate jobs)  
**Locale:** `es`  
**Source brief:** [brief-merged.md](./brief-merged.md)  
**Policy:** Global Leadership [sku-spine.md](../../../../../global-leadership/docs/locks/sku-spine.md)  
**Naming:** modules (`M##`), not units — `module_goal` not `unit_goal`

---

## Locked modules (order)

| ID | Tag | Working title | module_goal |
|----|-----|---------------|-------------|
| `M01` | core | Empezar por el propósito | Declarar en una frase para qué sirve el mensaje antes de volcar contenido. |
| `M02` | core | Completar el mensaje mínimo | Incluir contexto, qué, por qué importa, qué necesito y cuándo — sin adornos. |
| `M03` | core | Elegir el canal correcto | Emparejar chat, correo, llamada o reunión con riesgo, urgencia y necesidad de registro. |
| `M04` | core | Escuchar para entender | Separar oír del eco: resumir lo esencial del otro antes de empujar la propia posición. |
| `M05` | core | Confirmar comprensión compartida | Cerrar con un eco verificable de lo acordado — no con un “ok” fantasma. |
| `M06` | core | Escrito que acelera, no que confunde | Redactar chats y correos con propósito, pedido y próximo paso visibles en el primer pantallazo. |
| `M07` | complement | Puestas al día que no pierden gente | Estructurar actualizaciones orales para que cada rol sepa qué le toca. |
| `M08` | complement | Comunicar hacia arriba sin ruido | Subir información y pedidos con propósito, datos y decisión pedida — sin drama ni omisión. |
| `M09` | complement | Ruido en chats y reuniones híbridas | Reducir hilos muertos, micrófonos mudos y “¿me oyen?” que rompen la comprensión compartida. |

**ID map from brief:** `U01`–`U06` → `M01`–`M06`; complement pool → `M07`–`M09`.

---

## Assemble rules

- **Full provisional spine:** all 9 modules above.
- **Minimum assemble:** `M08` = all 6 core + any **2** of the complement set.
- **Shrink / short / intensive:** drop or defer **complement** first; heroes from **core** (`M01`–`M06`) only until slots fill.
- **Delivery shapes:** late assemble — do not regenerate a parallel taxonomy.
- **Tiers:** one spine for T1–T4; apply `tier_lenses.json` at asset generation.

---

## Handoff (from brief A3)

- **topic:** Retrasos y retrabajo causados por mensajes sin propósito, contexto incompleto, canal equivocado o “ok” sin comprensión compartida.
- **banned_phrases[]:** `Soft skills genérico sin comportamiento observable`, `“Comunicación efectiva” como frase vacía de cierre`, `Scripts de oratoria / storytelling motivacional`, `Estadísticas inventadas de “pérdida por mala comunicación”`
- **Next:** thin run tickets `CE · T1–T4 · es · M01` → generate demo assets; do not treat this file as Stage 3 content.
