# Fee-complete offer research and contribution

Read when the task asks for pricing, profit, shipping economics or an offer recommendation. It does not authorize changing price, shipping, ads or discounts. Reuse readable current seller/product decisions; avoid a new questionnaire. If country/currency/ad/tax facts remain unknown, calculate named scenarios and mark the unresolved fee rows instead of inventing a single net-profit number.

## Establish the calculation context

Record date; product/variant/quantity; item price after discount and paid personalization; buyer shipping/gift-wrap charges; supplier item/printing/shipping/handling/tax; destination/service; seller/bank-account country where relevant; listing/payment/settlement currencies; dated FX source; current ad status/attribution and applicable tax context. US buyers do not imply a US seller fee schedule. A Hong Kong owner or UI locale does not by itself establish bank-account country or settlement currency. Do not access private payment/identity data outside authority; use existing authorized facts or TBC/scenarios.

Use current official sources for rates and applicability: [Etsy Fees & Payments Policy](https://www.etsy.com/legal/fees/) and [Etsy Payments Policy](https://www.etsy.com/legal/etsy-payments/), plus their relevant official ad, regulatory-fee and tax help links. Store exact rate/fixed amount, currency, fee base, threshold/cap, condition, source URL/section, observed date and effective date if shown. A saved 2026-10-27 snapshot is historical evidence, not a current universal rate table. Do not hardcode this case's price or any country's fee rates into the Skill.

## Check every applicable fee, explicitly

For each row use `APPLICABLE_SOURCED`, `NOT_APPLICABLE` with reason, or `TBC`. Unknown is not zero. Read only relevant official sections and preserve the current research round's already-answered source order; no duplicate intake for the same round.

| Fee/cost category | What changes its amount or treatment |
|---|---|
| Listing / renewal / multi-quantity fees | Listing event versus order/unit allocation, actual sold quantities and renewal rule; do not double-count initial and allocated renewal without explaining the basis |
| Transaction fee | Current rate and exact taxable base: item, paid personalization, shipping, gift wrap and any jurisdiction-specific treatment |
| Etsy Payments processing | Seller/bank location, percentage **and fixed amount/currency**, full applicable order base including taxes where specified |
| Offsite Ads | Current eligibility/status, attribution, rate tier/cap/threshold; provide attributed and non-attributed scenarios if unknown |
| Etsy Ads | Actual or explicitly assumed allocated acquisition spend; it is not an automatic flat percentage of every sale |
| Currency conversion | Listing/payment currency mismatch and Etsy conversion fee/base; distinguish FX exchange rate from the extra fee and from buyer browsing conversion |
| Regulatory operating / governmental charges | Current relevant seller jurisdictions, rate/base and any separate levy; absence in another country is not proof of exemption |
| VAT/GST/sales tax on seller fees | Which fees are taxed, seller location/status and current tax basis; no tax-free assumption from display currency |
| Deposit / instant-transfer fees | Applicable market, thresholds, payout route and event allocation; do not charge every order unless that allocation is stated |
| Bank / Payoneer / other payout charges | Actual selected payout route and known fees; keep third-party charges distinct from Etsy fees |
| Shipping labels / insurance / handling | Only actual applicable costs; avoid double-counting supplier-paid postage and a label for the same shipment |
| Optional subscriptions / services / setup | Etsy Plus, Pattern, shop setup or other used services; separate one-off/fixed overhead allocation from marginal order contribution |
| Refunds / credits / adjustments | Actual applicable refunded-fee rules, return/reprint costs or clearly labeled scenario allowance; no unsupported historical return rate |
| Order taxes / duties | Buyer tax collected/remitted by Etsy, seller-borne tax and import costs are different; some fee bases may still include tax excluded from seller revenue |

This is an applicability checklist, not a claim every seller pays every row. Include any newly observed applicable fee from current official/account evidence rather than assuming this list fixes policy forever. Preserve cost source date, units, currency and tax-included/excluded basis.

## Calculate without false precision

Use one reporting currency with explicit conversion/rounding. Keep native-currency fixed fees and settlement uncertainty visible. Model each fee from its own base, not one universal percentage of item price.

```text
seller revenue = item price after discounts + paid options not already included
                 + buyer shipping + buyer gift-wrap charges
                 - any included tax collected/remitted for others
fulfillment cost = supplier item/print + supplier shipping + actual handling
                   + seller-borne non-recoverable tax/duties
known-cost subtotal = seller revenue - the explicitly listed known costs
estimated order contribution = seller revenue - fulfillment cost
                               - all applicable Etsy/payment/payout fees
                               - attributable ad/acquisition cost
                               - stated variable adjustment allowance
estimated contribution margin = estimated order contribution / seller revenue
```

Avoid double-counting paid personalization already in item price, tax already in supplier cost, a separately charged shipping label, or an FX fee already included in a quoted settlement amount. If a revenue denominator is zero/non-positive, do not report a normal margin percentage.

Order contribution is before any excluded fixed overhead, owner labor and income tax; identify those exclusions. Do not call it final take-home profit. If applicable fees remain TBC, label the result **known-cost subtotal with missing fees** or a clearly conditioned scenario, not fee-complete net contribution. A payment-account payout also is not profit.

When buyer shipping treatment is ambiguous, show both:

- **Buyer pays shipping:** buyer shipping charge is revenue; subtract actual supplier shipping and all applicable fees on that charge.
- **Seller offers free shipping:** buyer shipping charge is zero; supplier shipping still remains a cost. Recalculate fee bases and contribution rather than just deleting the displayed shipping line.

For ads, compare no-attributed-Offsite-Ads with the relevant attributed scenario where needed, without claiming either is the actual order state. Do not assume a discount, bundle, currency or seller country merely to produce a nicer margin.

## Recommendation and private-save boundary

Use [fee-offer-record.md](../assets/fee-offer-record.md) or an existing worksheet. Present the amount/range first, scenario assumptions, sourced applicable fees and remaining TBC. Compare candidate price/shipping combinations only within requested analytical scope. For a real change, show current → proposed exact values, expected contribution and assumptions, then reuse specific current owner authority or request the uncovered decision once. No autonomous commercial decision, live ad spend or shipping-profile change is granted here.

If the owner excludes shipping setup, preserve that exclusion. Economic scenarios can stay informative without reopening the excluded action or asserting a blank shipping profile is ready for release.
