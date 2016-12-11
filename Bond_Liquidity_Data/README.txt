"""
What are bonds?
A company needs funds to expand into new markets, while governments need money 
for everything from infrastructure to social programs. The problem large organizations 
run into is that they typically need far more money than the average bank can provide. 
The solution is to raise money by issuing bonds (or other debt instruments) to a public 
market. Thousands of investors then each lend a portion of the capital needed. Really, 
a bond is nothing more than a loan for which you are the lender. The organization that 
sells a bond is known as the issuer. You can think of a bond as an IOU given by a borrower 
(the issuer) to a lender (the investor).
Of course, nobody would loan his or her hard-earned money for nothing. The issuer of a bond 
must pay the investor something extra for the privilege of using his or her money. This "extra" 
comes in the form of interest payments, which are made at a predetermined rate and schedule. 
The interest rate is often referred to as the coupon. The date on which the issuer has to repay 
the amount borrowed (known as face value) is called the maturity date.

For example, say you buy a bond with a face value of $1,000, a coupon of 8%, and a maturity 
of 10 years. This means you'll receive a total of $80 ($1,000*8%) of interest per year for 
the next 10 years. Actually, because most bonds pay interest semi-annually, you'll receive 
two payments of $40 a year for 10 years. When the bond matures after a decade, you'll get 
your $1,000 back.

Maturity Type : 
Both investors and issuers are exposed to interest rate risk because they are locked into either 
receiving or paying a set coupon rate over a specified period of time. For this reason, some bonds 
offer additional benefits to investors or more flexibility for issuers
Callable, or a redeemable bond features gives a bond issuer the right, but not the obligation, 
to redeem his issue of bonds before the bond's maturity.
Convertible bonds give bondholders the right but not the obligation to convert their bonds into 
a predetermined number of shares at predetermined dates prior to the bond's maturity.
Puttable bonds give bondholders the right but not the obligation to sell their bonds back to the 
issuer at a predetermined price and date.

types of international bonds: 
A eurobond instead refers to any bond that is denominated in a currency other than that of the country in which it is issued.
Foreign bonds are denominated in the currency of the country in which a foreign entity issues the bond.
Global bonds are structured so that they can be offered in both foreign and eurobond markets.

Bankruptcy: 
Bonds represent debt which a company has agreed to repay with interest. As such, when a company 
files for federal bankruptcy protection, bondholders have a better chance of getting repaid 
than stockholders. While bankruptcy laws determine the order of repayment, stockholders, 
considered owners of the company, have the last claim on assets.
"""
"""
Data columns (total 24 columns):
isin                          17261  object	Unique Identification number to identify the bond.
issuer                        17261  object	Name of the Entity Issuing the Bond
issueDate                     17260  object	Date when the bond was issued
*market                        17261  object	Broad categorisation of bonds based on ratings and scope of trading
*amtIssued                     17261  float64 Total notional of bond when it was first issued
*amtOutstanding                17261  float64 Total tradable notional of bond remaining in market
collateralType                17261  object	Collateral (if any) posted against the issued debt.
coupon                        17261  float64 Coupon rate of bond
couponFrequency               16553  float64 Frequency with which coupons are paid in a year (annually, semi-annually, Quarterly, No Coupon)
couponType                    17261  object	Type of Coupon Rate eg. Fixed, floating, variable
*industryGroup                 17261  object	Intermediate level Industry Group classification of the issuer of the bond. Eg. Telecommunication, Banks, Health Industries
*industrySector                17261  object High level Industry Sector classification of the issuer of the bond. Eg. Communications, Financials, Consumer Non-Cyclical
*industrySubgroup              17261  object Lower level Industry Group classification of the issuer of the bond. Eg. Telephone-Integrated, Diversified Banking Inst, HealthCare Services
maturity                      17023  object	Type of Maturity of bond e.g. callable, convertible, perpetual, sinkable
maturityType                  17261  object When the bond gets paid out in full.
securityType                  17261  object	Defines the scope of trading of bond e.g. Euro-Dollar, US Domestic etc
paymentRank                   17261  object	The order of repayment in event of bankruptcy
144aFlag                      17261  object	Indicates if the bond was a 144a offering which places some restrictions on trade ability of bonds.
ratingAgency1Rating           17261  object	Rating issued by Credit Rating Agency 1 to assert the “credit quality” of bond
ratingAgency1Watch            17261  object	Indication if Rating agency 1 is considering taking any action (e.g. upgrade, downgrade. no-action) regarding the rating of product
ratingAgency1EffectiveDate    15480  object Date when Rating agency 1 last rated the product.
ratingAgency2Rating           17261  object Rating issued by Credit Rating Agency 2 to assert the “credit quality” of bond
ratingAgency2Watch            17261  object Indication if Rating agency 2 is considering taking any action (e.g. upgrade, downgrade. no-action) regarding the rating of product
ratingAgency2EffectiveDate    15995  object Date when Rating agency 2 last rated the product. 

"""
