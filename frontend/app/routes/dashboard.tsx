/**
 * Dashboard Page (Protected Route)
 */

import type { Route } from "./+types/dashboard";
import { useAuthRequired } from "~/lib/hooks";
import { Box, Heading, Grid, GridItem, VStack, Spinner, Container, Text } from "@chakra-ui/react";
import { Card } from "~/components/common";

export const meta: Route.MetaArgs = () => [
  { title: "Dashboard - webapp-template" },
  { name: "description", content: "Your dashboard" },
];

export default function DashboardPage() {
  const { isAuthenticated, isChecking } = useAuthRequired();

  if (isChecking) {
    return (
      <Box minH="screen" display="flex" alignItems="center" justifyContent="center">
        <Spinner size="lg" color="blue.600" />
      </Box>
    );
  }

  if (!isAuthenticated) {
    return null;
  }

  return (
    <Container maxW="7xl" py={12} px={{ base: 4, sm: 6, lg: 8 }}>
      <Heading as="h1" size="2xl" mb={8}>Dashboard</Heading>

      <Grid templateColumns={{ base: "1fr", md: "repeat(2, 1fr)", lg: "repeat(3, 1fr)" }} gap={6} mb={8}>
        <GridItem>
          <Card>
            <Heading as="h3" size="md" mb={2}>Total Users</Heading>
            <Text fontSize="3xl" fontWeight="bold" color="blue.600">0</Text>
          </Card>
        </GridItem>

        <GridItem>
          <Card>
            <Heading as="h3" size="md" mb={2}>Active Sessions</Heading>
            <Text fontSize="3xl" fontWeight="bold" color="green.600">0</Text>
          </Card>
        </GridItem>

        <GridItem>
          <Card>
            <Heading as="h3" size="md" mb={2}>API Calls</Heading>
            <Text fontSize="3xl" fontWeight="bold" color="purple.600">0</Text>
          </Card>
        </GridItem>
      </Grid>

      <Card>
        <Heading as="h2" size="lg" mb={4}>Welcome to your Dashboard</Heading>
        <Text color="gray.600">
          This is a protected route that requires authentication. You can add your dashboard content here.
        </Text>
      </Card>
    </Container>
  );
}