import { createRegionsWorkflow } from "@medusajs/core-flows"
import { MedusaContainer } from "@medusajs/framework/types"

export default async function seedRegion(container: MedusaContainer) {
  await createRegionsWorkflow(container).run({
    input: {
      regions: [
        {
          name: "Togo",
          currency_code: "xof",
          countries: ["tg"],
        },
      ],
    },
  })
  console.log("✅ Région Togo (XOF) créée avec succès !")
}
